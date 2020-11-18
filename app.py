from flask import Flask, render_template, url_for, request, redirect, make_response
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb, Movie 
import os
import pickle
import recommender_system
import tmdb_api_script
import justwatch_scraper
import buildOP

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

tmdb = TMDb() 
tmdb.api_key = 'e37d84894950becf35214f1f9ab0e0a9'
    
@app.route('/', methods=['POST', 'GET'])

def main():
    if request.method == 'GET':
        response = make_response(render_template('index.html'))
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        
        return response

    if request.method == 'POST':
        title = request.form['title']
        # print(request.form)
        # print()
        # print(request.form['title'])
        
        metadata = tmdb_api_script.call_api(title)
        
        reco = recommender_system.recommender_system(metadata)
        
        results = {}
        # print(reco['title'])
        
        for i in reco['title']: 
            results[i.title()] = justwatch_scraper.get_links(i)
        
        # print(results) 
        
        display = buildOP.build_display(metadata['title'][0].title(), results) 
        display_file= open("templates/display.html","w")
        display_file.write(display)
        display_file.close()
        
        # print(display)
        
        response = make_response(render_template('display.html'))
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        
        return response

if __name__ == '__main__':
    app.run(debug=True)
    
