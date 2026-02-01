from django.shortcuts import render
from .models import Item
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def index(request):
    return render(request, 'index.html')

def recommend(request):
    if request.method == 'POST':
        # 1. Capture User Input Vector from Form
        try:
            user_vector = [
                float(request.POST.get('acidity', 0)),
                float(request.POST.get('body', 0)),
                float(request.POST.get('sweetness', 0)),
                float(request.POST.get('bitterness', 0)),
                float(request.POST.get('aroma', 0)),
                float(request.POST.get('texture', 0)),
                # Caffeine is not in the slider yet, assume 0 or handle separately
                0.0 
            ]
        except ValueError:
            return render(request, 'index.html', {'error': 'Invalid input'})

        # 2. Load Data from DB
        items = Item.objects.all()
        if not items.exists():
            return render(request, 'result.html', {'recommendations': [], 'user_vector': user_vector})

        # 3. Create DataFrame for Analysis
        item_data = []
        for item in items:
            vec = item.get_vector()
            # Ensure vector length matches
            item_data.append(vec)
        
        # 4. Calculate Similarity using Scikit-Learn
        # User vector needs to be 2D array [1, n_features]
        X = np.array(item_data)
        Y = np.array([user_vector])
        
        # Cosine Similarity returns a matrix, we take the first row
        scores = cosine_similarity(X, Y).flatten()
        
        # 5. Rank Results
        # Combine items with scores
        results = zip(items, scores)
        # Sort by score descending
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        
        # Context preparation (Top 5)
        # Convert score to percentage for display
        final_recommendations = [(item, score * 100) for item, score in sorted_results[:5]]

        return render(request, 'result.html', {
            'recommendations': final_recommendations,
            'user_vector': user_vector
        })

    return render(request, 'index.html')
