from yattag import Doc

def build_display(input, dictRes): 
    doc, tag, text = Doc().tagtext() 
    
    with tag('html'): 
        doc.stag('link', rel="stylesheet", type="text/css", href="{{ url_for('static',filename='styles/style.css') }}")
        
        with tag('head'): 
            with tag('title'): 
                text('Mo\'s Movie Recommendation Engine')
                
        with tag('h1', align="center"): 
            text('Mo\'s Top Recommendations:')
            
        with tag('h3', align="center"):
            text('Now showing movies similar to \"{0}\"'.format(input))
            
        with tag('div', klass="result", align="center"):
            with tag('table', width="100%"): 
                with tag('tr'): 
                    with tag('th'): 
                        text('MOVIE') 
                    with tag('th'): 
                        text('WATCH IT HERE')
                        
                for movie in dictRes: 
                    with tag('tr'): 
                        with tag('td'): 
                            text(movie.title()) 
                            
                        with tag('td'):
                            if (len(dictRes[movie]) == 0): 
                                text('Sorry. We could not find any links to this movie in your region.')
                                
                            with tag('table', id="table01"):
                                for category in dictRes[movie]: 
                                    with tag('tr'): 
                                        with tag('td', id="table01", style="padding:2px; background-color:#282828; color:white; align:center;"): 
                                            with tag('div', id="link-category"): 
                                                text(category.upper())
                                                
                                        with tag('td', id="table01"):
                                            with tag('table'): 
                                                with tag('tr'): 
                                                    for link in dictRes[movie][category]: 
                                                        with tag('td'): 
                                                            with tag('a', href=link, target="_blank"): 
                                                                doc.stag('img', src=dictRes[movie][category][link]['src'], klass="provider-icon", width="50", height="50")
                                                                # text(dictRes[movie][category][link]['src']) 
                                                                
            
            with tag('a', href="{{ url_for('main') }}", klass="btn btn-default"): 
                text('Back')
                                                                
    return doc.getvalue()