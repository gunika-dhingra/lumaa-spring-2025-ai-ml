
# Overview
This project is a News Recommendation System that allows users to input a query and receive top news articles that are most relevant to their search. The recommendation is based on TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity.

# Features 
* Query-based news recommendations: Users can enter a search term and get relevant news articles.
* Category Filtering: Users can select one or multiple categories to filter results.
* "I am open to any category" option: Allows users to receive recommendations from all categories.
* Efficient TF-IDF + Cosine Similarity Matching: Provides accurate text-based recommendations.
* User-Friendly Streamlit Interface: Interactive and easy to use.

# Dataset
The system is built using the [AG News Classification Dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset/data?select=train.csv), which contains news articles categorized into four labels:
1. World
2. Sports
3. Business
4. Science/Technology

# How It Works
### Load and Preprocess the Data
- Clean and preprocess text (remove punctuation, stopwords, lowercase conversion).
- Combine Title and Description for better textual representation.

### Train TF-IDF Model
- Convert preprocessed text into numerical vectors.
- Compute the similarity between news articles and user query using Cosine Similarity.

### Category Filtering
- Users can select categories to filter recommendations.
- If "I am open to any category" is selected, recommendations are provided from all categories.

### Generate Recommendations
- The system retrieves top N most relevant articles based on similarity scores.

# Installation & Setup
### Cloning the repository
```
git clone https://github.com/gunika-dhingra/lumaa-spring-2025-ai-ml.git
```
### Prerequisites
Ensure you have Python 3.x installed along with the necessary dependencies:
```sh
pip install requirements.txt
```
### Run the streamlit app
```sh
streamlit sun recommend.py
```
# Usage
- Enter a query (e.g., "Latest AI advancements").
- Select preferred categories (e.g., "Sci/Tech" and "Business").
- View recommended news articles.

# Video Demo
The video demo of the project can be accessed [here.](https://www.loom.com/share/2a56d0d161f5452482f3072dc12795c3?sid=70922871-4be5-4a94-987e-4a8ff396ed70) 

Another example of the working can be accessed [here.](https://www.loom.com/share/d7a342e0631f42d29c8b92f8b1e11d40?sid=f8e7435d-f3f4-46fd-8042-4211ce51598c)


# Salary Expectation

As a full-time student with a strong background in AI and ML, complemented by my undergraduate studies and internship experiences, I expect a compensation of around $35–$45 per hour for this internship. However, I am open to discussing this further based on the role’s responsibilities and the overall compensation structure

---
Made with ❤️ by Gunika
