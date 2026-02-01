# ☕ Coffee & Tea Recommendation Service

A **Django-based recommendation system** that suggests coffee, tea, and food based on user taste preferences (Acidity, Body, Sweetness, etc.) using **Scikit-learn** and **Cosine Similarity**.

## 📌 Features

- **Hybrid Data Model**: 
  - `FlavorVectorMixin`: Stores analytical data (Acidity, Body, etc.) as `FloatFields` for vector calculation.
  - `Item`: Stores extensible attributes (Origin, Type, Calories) in a `JSONField`.
- **Recommendation Engine**:
  - Converts user input and database items into feature vectors.
  - Calculates similarity using `sklearn.metrics.pairwise.cosine_similarity`.
- **Modern UI**: Dark-themed, responsive design using Django Templates & CSS.

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository (if applicable) or navigate to the directory
cd coffee_service

# Create Virtual Environment (Optional but recommended)
python -m venv venv
# Windows:
.\venv\Scripts\Activate
# Mac/Linux:
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Apply migrations
python manage.py migrate

# (Optional) Populate sample data
python populate_data.py
```

### 3. Run Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to try the recommender!

## 📂 Project Structure

- `core/models.py`: Defines `Item`, `FlavorVectorMixin` (Hybrid Model Design).
- `core/views.py`: Implements vector creation and Scikit-learn similarity logic.
- `populate_data.py`: Script to generate test data (Coffee, Tea, Cake).
- `templates/`: HTML files (`index.html`, `result.html`).
