from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, static_url_path='/static')

# Load your movie data and prepare necessary data structures
movies = pd.read_csv('./data/movies.csv')  # Update with your data file

# Content-Based Filtering (using movie overviews)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['overview'].fillna(''))
cosine_sim_content = cosine_similarity(tfidf_matrix)

# Build the item-item matrix using the DataFrame index
item_item_matrix = movies.pivot(columns='title', values='vote_average')

# Calculate the cosine similarity between the items (movies) based on the item-item matrix
cosine_sim_collaborative = cosine_similarity(item_item_matrix.fillna(0))

# Content-Enhanced Recommender Function
def content_enhanced_recommender(movie_title, movie_data, cosine_sim_content, cosine_sim_collaborative):
    target_movie_index = movies.index[movies['title'] == movie_title].tolist()[0]
    
    # Get content-based similarity scores for the target movie
    content_scores = cosine_sim_content[target_movie_index]

    # Get collaborative similarity scores for movies similar to the target movie based on ratings
    collaborative_scores = cosine_sim_collaborative[target_movie_index]

    # Combine content-based and collaborative scores
    hybrid_scores = content_scores + collaborative_scores

    # Get indices of top 5 movies based on hybrid scores
    top_indices = hybrid_scores.argsort()[::-1][1:6]

    # Get the titles of the top 5 recommended movies
    recommended_movies = movies.iloc[top_indices]['title']
    return recommended_movies    

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_movies = []  # Initialize recommended_movies as an empty list

    if request.method == 'POST':
        movie_title = request.form['movie_title']
        
        if movie_title in movies['title'].values:
            recommended_movies = content_enhanced_recommender(movie_title, movies, cosine_sim_content, cosine_sim_collaborative)
            print(recommended_movies)
        else:
            recommended_movies = ['None found in database']
    
    return render_template('index.html', recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
