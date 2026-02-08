from django.shortcuts import render, redirect
from .models import Question, Choice, Product, FlavorProfile, Category

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'core/index.html', context)

def quiz_view(request):
    # Show only general user questions (not expert mode)
    questions = Question.objects.filter(is_expert=False).prefetch_related('choices').order_by('order')
    return render(request, 'core/quiz.html', {'questions': questions})

def quiz_result(request):
    if request.method != 'POST':
        return redirect('quiz')

    # Calculate scores
    scores = {
        'acidity': 0, 'body': 0, 'sweetness': 0, 
        'bitterness': 0, 'aroma': 0, 'aftertaste': 0
    }
    
    for key, value in request.POST.items():
        if key.startswith('q_'):
            try:
                choice_id = int(value)
                choice = Choice.objects.get(id=choice_id)
                scores['acidity'] += choice.acidity_score
                scores['body'] += choice.body_score
                scores['sweetness'] += choice.sweetness_score
                scores['bitterness'] += choice.bitterness_score
                scores['aroma'] += choice.aroma_score
                scores['aftertaste'] += choice.aftertaste_score
            except (ValueError, Choice.DoesNotExist):
                continue

    # Store scores in session for potential expert mode continuation
    request.session['general_scores'] = scores

    # Assign Title based on flavor profile
    # TODO: This is a simple placeholder algorithm. Will be enhanced with more sophisticated logic.
    title = assign_coffee_title(scores)

    # Find Recommendations using simple distance algorithm
    # TODO: This is a placeholder algorithm. Can be enhanced with more sophisticated matching later.
    products = Product.objects.all()
    
    # Calculate difference score for each product
    scored_products = []
    for p in products:
        fp = p.flavor_profile
        diff = (
            abs(fp.acidity - scores['acidity']) +
            abs(fp.body - scores['body']) +
            abs(fp.sweetness - scores['sweetness']) +
            abs(fp.bitterness - scores['bitterness']) +
            abs(fp.aroma - scores['aroma']) +
            abs(fp.aftertaste - scores['aftertaste'])
        )
        scored_products.append((diff, p))
    
    scored_products.sort(key=lambda x: x[0])
    recommendations = [p for _, p in scored_products[:3]]

    # Prepare data for radar chart (for expert mode)
    chart_data = {
        'labels': ['산미', '바디감', '단맛', '쓴맛', '향', '후미'],
        'values': [
            scores['acidity'],
            scores['body'],
            scores['sweetness'],
            scores['bitterness'],
            scores['aroma'],
            scores['aftertaste']
        ]
    }

    context = {
        'scores': scores,
        'recommendations': recommendations,
        'chart_data': chart_data,
        'title': title['title'],
        'description': title['description'],
    }
    return render(request, 'core/result.html', context)

def assign_coffee_title(scores):
    """
    Assign a coffee personality title based on flavor profile scores.
    Maps to natural language interpretations without technical jargon.
    """
    # Calculate dominant characteristics
    max_score = max(scores.values())
    
    # Determine which attributes are dominant
    acidity_high = scores['acidity'] >= 12  # High threshold for acidity
    bitterness_high = scores['bitterness'] >= 10
    body_high = scores['body'] >= 12
    aftertaste_high = scores['aftertaste'] >= 13
    
    # Category 1: 산뜻한 과일형 (Fresh Fruit Type)
    # High acidity, low bitterness, clean aftertaste
    if acidity_high and scores['bitterness'] < 8:
        return {
            'title': '산뜻한 과일형',
            'description': '신맛이 튀지 않으면서도 입안이 깔끔하게 정리되는 커피를 선호하는 편이에요. 가볍게 마시기 좋은 인상을 중요하게 여겨요.'
        }
    
    # Category 2: 묵직한 블랙형 (Heavy Black Type)
    # High bitterness, medium-high body
    elif bitterness_high and body_high:
        return {
            'title': '묵직한 블랙형',
            'description': '너무 가볍지 않고 맛의 중심이 분명한 커피에서 만족감을 느끼는 편이에요. 한 모금만으로도 존재감이 느껴지는 쪽이 잘 맞아요.'
        }
    
    # Category 3: 여운 중시 (Aftertaste-focused)
    # High body, strong aftertaste
    elif aftertaste_high or (body_high and scores['aftertaste'] >= 11):
        return {
            'title': '여운 중시',
            'description': '마셨을 때 밀도감이 느껴지는 진한 인상의 커피를 편하게 느끼는 편이에요. 향과 맛이 천천히 남는 걸 좋아해요.'
        }
    
    # Category 4: 안정된 밸런스형 (Stable Balance Type)
    # Balanced, smooth aftertaste, low bitterness
    else:
        return {
            'title': '안정된 밸런스형',
            'description': '과하지 않고 안정적인 맛의 커피를 선호해요. 마신 뒤 인상이 편안하게 남는 게 중요해요.'
        }

def expert_quiz_view(request):
    # Get general scores from session
    general_scores = request.session.get('general_scores')
    if not general_scores:
        return redirect('quiz')  # Must complete general quiz first
    
    # Show expert questions
    questions = Question.objects.filter(is_expert=True).prefetch_related('choices').order_by('order')
    return render(request, 'core/expert_quiz.html', {'questions': questions})

def expert_result(request):
    if request.method != 'POST':
        return redirect('expert_quiz')
    
    # Get general scores from session
    general_scores = request.session.get('general_scores', {
        'acidity': 0, 'body': 0, 'sweetness': 0,
        'bitterness': 0, 'aroma': 0, 'aftertaste': 0
    })
    
    # Calculate expert scores
    expert_scores = {
        'acidity': 0, 'body': 0, 'sweetness': 0,
        'bitterness': 0, 'aroma': 0, 'aftertaste': 0
    }
    
    for key, value in request.POST.items():
        if key.startswith('q_'):
            try:
                choice_id = int(value)
                choice = Choice.objects.get(id=choice_id)
                expert_scores['acidity'] += choice.acidity_score
                expert_scores['body'] += choice.body_score
                expert_scores['sweetness'] += choice.sweetness_score
                expert_scores['bitterness'] += choice.bitterness_score
                expert_scores['aroma'] += choice.aroma_score
                expert_scores['aftertaste'] += choice.aftertaste_score
            except (ValueError, Choice.DoesNotExist):
                continue
    
    # Combine scores (weighted average or simple addition - can be customized)
    # TODO: Implement more sophisticated score combination formula
    combined_scores = {
        'acidity': general_scores['acidity'] + expert_scores['acidity'],
        'body': general_scores['body'] + expert_scores['body'],
        'sweetness': general_scores['sweetness'] + expert_scores['sweetness'],
        'bitterness': general_scores['bitterness'] + expert_scores['bitterness'],
        'aroma': general_scores['aroma'] + expert_scores['aroma'],
        'aftertaste': general_scores['aftertaste'] + expert_scores['aftertaste'],
    }
    
    # Find recommendations with combined scores
    products = Product.objects.all()
    scored_products = []
    for p in products:
        fp = p.flavor_profile
        diff = (
            abs(fp.acidity - combined_scores['acidity']) +
            abs(fp.body - combined_scores['body']) +
            abs(fp.sweetness - combined_scores['sweetness']) +
            abs(fp.bitterness - combined_scores['bitterness']) +
            abs(fp.aroma - combined_scores['aroma']) +
            abs(fp.aftertaste - combined_scores['aftertaste'])
        )
        scored_products.append((diff, p))
    
    scored_products.sort(key=lambda x: x[0])
    recommendations = [p for _, p in scored_products[:3]]
    
    # Prepare chart data
    chart_data = {
        'labels': ['산미', '바디감', '단맛', '쓴맛', '향', '후미'],
        'values': [
            combined_scores['acidity'],
            combined_scores['body'],
            combined_scores['sweetness'],
            combined_scores['bitterness'],
            combined_scores['aroma'],
            combined_scores['aftertaste']
        ]
    }
    
    context = {
        'scores': combined_scores,
        'recommendations': recommendations,
        'chart_data': chart_data,
        'is_expert_result': True,
    }
    return render(request, 'core/expert_result.html', context)

# Daily Recommendation Views
from django.http import JsonResponse
import random

def daily_recommendation(request):
    """
    Daily coffee recommendation page.
    Shows random coffee or preference-based if quiz completed.
    """
    # Check if user has quiz results
    if 'general_scores' in request.session:
        scores = request.session['general_scores']
        recommendations = get_recommendations_list(scores)
        coffee = recommendations[0] if recommendations else get_random_coffee()
        has_preferences = True
    else:
        coffee = get_random_coffee()
        has_preferences = False
    
    context = {
        'coffee': coffee,
        'has_preferences': has_preferences
    }
    return render(request, 'core/daily_recommendation.html', context)

def get_random_coffee():
    """Get a random coffee product."""
    coffees = list(Product.objects.all())
    return random.choice(coffees) if coffees else None

def get_recommendations_list(scores):
    """Get ordered list of coffee recommendations based on scores."""
    products = Product.objects.all()
    
    scored_products = []
    for p in products:
        fp = p.flavor_profile
        diff = (
            abs(fp.acidity - scores['acidity']) +
            abs(fp.body - scores['body']) +
            abs(fp.sweetness - scores['sweetness']) +
            abs(fp.bitterness - scores['bitterness']) +
            abs(fp.aroma - scores['aroma']) +
            abs(fp.aftertaste - scores['aftertaste'])
        )
        scored_products.append((diff, p))
    
    scored_products.sort(key=lambda x: x[0])
    return [p for _, p in scored_products]

def get_next_recommendation(request):
    """API endpoint to get next best recommendation."""
    current_id = request.GET.get('current_id')
    
    if 'general_scores' in request.session:
        scores = request.session['general_scores']
        recommendations = get_recommendations_list(scores)
        
        # Find current coffee in recommendations and get next one
        current_index = -1
        for i, coffee in enumerate(recommendations):
            if str(coffee.id) == current_id:
                current_index = i
                break
        
        next_index = (current_index + 1) % len(recommendations)
        next_coffee = recommendations[next_index]
    else:
        # Get random coffee if no preferences
        next_coffee = get_random_coffee()
    
    return JsonResponse({
        'id': next_coffee.id,
        'name': next_coffee.name,
        'description': next_coffee.description,
        'image_url': next_coffee.image.url if next_coffee.image else ''
    })

def roulette_recommendation(request):
    """API endpoint for roulette selection."""
    if 'general_scores' in request.session:
        scores = request.session['general_scores']
        recommendations = get_recommendations_list(scores)
        coffee_pool = recommendations[:10]  # Top 10 recommendations
    else:
        coffee_pool = list(Product.objects.all()[:10])  # Get 10 random coffees
    
    selected = random.choice(coffee_pool) if coffee_pool else None
    
    if selected:
        return JsonResponse({
            'id': selected.id,
            'name': selected.name,
            'description': selected.description,
            'image_url': selected.image.url if selected.image else '',
            'pool': [{'id': c.id, 'name': c.name} for c in coffee_pool]
        })
    
    return JsonResponse({'error': 'No coffees available'}, status=404)

def roulette_page(request):
    """Roulette page view."""
    return render(request, 'core/roulette.html')
