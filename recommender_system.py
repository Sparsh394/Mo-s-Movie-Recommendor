import pandas as pd #library import
import json
from collections import ChainMap
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel, cosine_similarity
import numpy as np
from ast import literal_eval
movie_df=pd.read_csv(r"tmdb_5000_movies.csv") #reading data
movie_df['genres'] = movie_df['genres'].apply(literal_eval) #applying preprocessing and removing unwanted data
movie_df['keywords'] = movie_df['keywords'].apply(literal_eval)
movie_df['genres'] = movie_df['genres'].apply(lambda x: [y['name'] for y in x])
movie_df['keywords'] = movie_df['keywords'].apply(lambda x: [y['name'] for y in x])
movie_df[['genres', 'keywords']][:1]
movie_df['spoken_languages'] = movie_df['spoken_languages'].apply(literal_eval)
movie_df['spoken_languages'] = movie_df['spoken_languages'].apply(lambda x: [y['name'] for y in x])
movie_df.drop(columns=['budget','original_title','production_companies','production_countries','spoken_languages'],inplace=True)

movie_df['description']=movie_df['tagline'].fillna(" ")+" "+movie_df['overview'].fillna(" ")
movie_df['title']=movie_df['title'].str.lower()
movie_df['description']=movie_df['description'].str.lower()
# sample_row=movie_df.sample(n=1) #sample row that will be replaced by code to integrate data returned by TMDB scraping API 

def recommender_system(movie_metadata): #recommender function
    print(movie_metadata)
    global movie_df
    movie_metadata['title']=movie_metadata['title'].str.lower()
    movie_metadata['description']=movie_metadata['tagline'].fillna(" ")+" "+movie_metadata['overview'].fillna(" ")
    movie_metadata['description']=movie_metadata['description'].str.lower()
    tfidf=TfidfVectorizer(stop_words='english')
    title_check=movie_metadata.iloc[0]['title']
    if(title_check not in (movie_df['title'].tolist())):
        movie_df=movie_df.append(movie_metadata)
        movie_df.reset_index(inplace=True)
    tfidf_matrix=tfidf.fit_transform(movie_df['description'].apply(lambda x: np.str_(x)))
    cosine_similarity=sigmoid_kernel(tfidf_matrix,tfidf_matrix)
    indices = pd.Series(movie_df.index, index=movie_df['title'])
    #print(indices.tail())
    #print(movie_df['title'].tail())
    title_req=movie_metadata.iloc[0]['title']
    print('title: ',title_req)
    required_index=indices[title_req]
    sim_scores = list(enumerate(cosine_similarity[required_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    required_movies=movie_df.iloc[movie_indices]
    print(required_movies['title'])
    required_movies=required_movies.sort_values('vote_average',ascending=False)
    return required_movies
    
# print(recommender_system(sample_row)) #placeholder for testing
