#importing necessary libraries
import pandas as pd
import re
import string 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

nltk.download('stopwords')
nltk.download('punkt_tab')

stopwords = set(stopwords.words('english'))


#load the training set of the AG News dataset
data = pd.read_csv('train.csv')


# text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{string.punctuation}]', ' ',text)
    text = ' '.join([word for word in word_tokenize(text)])
    return text
    

data['processed_text'] = (data['Title']+ ' ' + data['Description']).apply(preprocess_text)
category_mapping = {
    1: 'World',
    2:'Sports',
    3: 'Business',
    4: 'Sci/Tech'
}
data['Class Index'] = data['Class Index'].map(category_mapping)
# defining the vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
tfidf_matrix = vectorizer.fit_transform(data['processed_text'])


def recommeder(query,selected_categories, n=3):
    query_processed = preprocess_text(query)
    query_vector = vectorizer.transform([query_processed])
    similarity_score = cosine_similarity(query_vector,tfidf_matrix).flatten()
    if 'I am open to any category' not in selected_categories:
        filtered_news = data[data['Class Index'].isin(selected_categories)]
    else:
        filtered_news = data
    filtered_indices = filtered_news.index.tolist()
    similarity_filter = [(i,similarity_score[i]) for i in filtered_indices]
    similarity_filter = sorted(similarity_filter, key=lambda x:x[1], reverse=True)
    top_indices = [i[0] for i in similarity_filter[:n]]
    return data.iloc[top_indices][['Title','Description','Class Index']]
# streamlit code for web UI
st.title('News Recommender System')
query = st.text_input('Enter your query')
st.write('## Select a category of news you might like: ')
category_options = list(category_mapping.values())  
selected_categories = []

for category in category_options:
    if st.checkbox(category, value= True):
        selected_categories.append(category)

if st.checkbox('I am open to any category', value=True):
    selected_categories=['I am open to any category']

if query:
    recommended_articles = recommeder(query,selected_categories, n=4)
    st.write('### Recommended Arcticles')
    
    for i, row in recommended_articles.iterrows():
           st.write(f"**{row['Title']}**")
           st.write(f"*Category: {row['Class Index']}*")
           st.write(f"{row['Description']}")
           st.write('---')