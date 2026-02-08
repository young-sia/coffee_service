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
