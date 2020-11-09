from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb, Movie 
import os
import pickle
import recommender_system
import tmdb_api_script

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

tmdb = TMDb() 
tmdb.api_key = 'e37d84894950becf35214f1f9ab0e0a9'
    
# recommender = pickle.load(open(r'recommender_function.sav', 'rb'))
# apiCall = pickle.load(open(r'call_api.sav', 'rb'))
    
@app.route('/', methods=['POST', 'GET'])

def main():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # recommender = pickle.load(open(r'recommender_function.sav', 'rb'))
        
        title = request.form['title']
        
        # df=pd.read_csv("tmdb_5000_movies.csv")
        # metadata = df.loc[df['title'] == title.str.lower()]
        
        # metadata = apiCall(title)
        metadata = tmdb_api_script.call_api(title)
        
        print('Queried movie: ')
        print(metadata)
        
        # reco = recommender(metadata)
        reco = recommender_system.recommender_system(metadata)
        
        print('The recommended movies are: \n')
        print(reco['title'])
        
        recommendations = []
        
        for i in reco['title']: 
            recommendations.append(i.title())
        
        result = {'reco': recommendations}
        inputTitle = {'title': metadata['title'][0].title()}
        
        return render_template('show.html', original_input = inputTitle, result=result)

if __name__ == '__main__':
    # recommender = pickle.load(open(r'recommender_function.sav', 'rb'))
    app.run(debug=True)
    
