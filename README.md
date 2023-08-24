# Problem Statement

Develop a personalized Movie Recommender System that leverages both content and collaborative filtering algorithms to recommend movies based on user preferences and voting average behaviors. The aim is to provide users with tailored movie recommendations, enhancing their entertainment experience and helping them discover other movies aligned with their tastes.


## Overview

In today's digital age, the abundance of movie choices often leads to decision fatigue for users looking to find films that match their interests. A reliable recommendation system can alleviate this issue by intelligently analyzing movies' content and voting average to suggest movies they are likely to enjoy. Collaborative filtering, a popular recommendation technique, utilizes the collective preferences and behaviors of users such as the voting average. In addition to collaborative filtering, our Movie Recommender System incorporates content-based filtering techniques to enhance the accuracy and diversity of movie recommendations. Content-based filtering focuses on the attributes of the movies themselves, analyzing features such as plot keywords to suggest movies that are structurally similar to those a user has shown interest in.

The integration of collaborative filtering and content-based filtering in the Movie Recommender System creates a synergistic effect. Collaborative filtering taps into user preferences and behaviors, while content-based filtering considers the intrinsic attributes of movies. Together, these techniques provide a more comprehensive, accurate, and diverse set of movie recommendations, helping users discover movies they are likely to enjoy without being overwhelmed by the sheer number of choices.

## Project Workflow

The Movie Recommender System will be developed using Python and the Flask web framework. It will involve the following key components:

- Data Import and Preparation: Import movie data from an external source and process it to create a usable dataset. This will include movie details, and voting averages.

- Movie Recommender System employs a hybrid approach, combining both collaborative filtering and content-based filtering techniques to provide users with a comprehensive and tailored movie recommendation experience.

- Web Interface: Develop a user-friendly web interface that allows users to create accounts, rate movies, and receive recommendations. The interface will also include options for filtering and exploring movie details.

## Data Collection

About 10000 movies with their respective content and voting average are obtained from TMDB movie database. 

## EDA

### Data Cleaning

Remove movies that have null content.  

## Preprocessing

### NLP Processing Steps

1. Tokenization the all movie content.
2. Lemmatization all the token words from above step.
3. TfidfVectorizer the tokenized/lemmatized words.

## Recommender

For content-based filtering, cosine similarity is used to measure the likeness between the content of the user's chosen movie and the content of different movies.

For collaborative filtering aspect, we also utilize cosine similarity to evaluate the resemblance between the different movies based on their voting averages. Each movie's voting averages form a vector that characterizes their popularity. By calculating the cosine similarity between voting averages' vectors, we can identify movies that are generally popular with the mass audiences.

## Conclusions

From the Flask app created for the Movie Recommender system, the user will input a movie's name inside the input box, and the Movie Recommender system will generate the top 5 movies recommendations.

## Recommendations

- Real-time Updates: Implement a mechanism to provide real-time updates for movie data and user interactions. This ensures that recommendations stay current and reflective of the latest trends and user preferences.
- Localization: If applicable, provide recommendations based on users' language preferences and regional content availability.