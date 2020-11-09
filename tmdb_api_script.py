from tmdbv3api import TMDb #import libraries
from tmdbv3api import Movie
import pandas as pd
tmdb = TMDb() #initiate API with key
tmdb.api_key = 'e37d84894950becf35214f1f9ab0e0a9'
from ast import literal_eval
movie=Movie() 
input_term=input()
def call_api(input_term): #call TMDB API first for search then for the rest of the movie details
    search = movie.search(input_term)
    res_id=search[0].id
    res=movie.details(res_id)
    movie_metadata=pd.DataFrame(columns=['genres','homepage','id','keywords','original_language','overview','popularity','release_date','revenue','runtime','status','tagline','vote_average','vote_count'])
    movie_metadata.at[0,'genres']=res.genres
    #movie_metadata['genres'] = movie_metadata['genres'].apply(literal_eval)
    #movie_metadata['genres'] = movie_metadata['genres'].apply(lambda x: [y['name'] for y in x])
    movie_metadata['homepage']=res.homepage
    movie_metadata['id']=res.id
    movie_metadata['keywords']=''
    movie_metadata['original_language']=res.original_language
    movie_metadata['overview']=res.overview
    movie_metadata['popularity']=res.popularity
    movie_metadata['release_date']=res.release_date
    movie_metadata['revenue']=res.revenue
    movie_metadata['runtime']=res.runtime
    movie_metadata['status']=res.status
    movie_metadata['tagline']=res.tagline
    movie_metadata['title']=res.title
    movie_metadata['vote_average']=res.vote_average
    movie_metadata['vote_count']=res.vote_count
    return movie_metadata
print(call_api(input_term))
    
    
    
    