import flask
import buildOP

app = flask.Flask(__name__, template_folder='templates')

a = {'age': 21, 'name': 'Sparsh'}

print(a['name'])

b = { 'iron man': {'stream': { 'hotstar': {'src': 'img1'}, 'netflix': {'src': 'img2'}}, 'buy': {'Play Movies': {'src': 'img4'}}}, 
    'avatar': {'rent': {'Play Movies': {'src': 'img4'}}}} 

# output_html = "<table>\n"

# # Create the table's column headers
# output_html += "  <tr>\n"  
# output_html += "    <th>MOVIE</th>\n    <th>WATCH IT HERE</th>\n"
# output_html += "  </tr>\n"

# # Create the table's row data
# for movie in b:
    # output_html += "  <tr>\n    <td>{0}</td>\n".format(movie.title())
    # output_html += "    <td>\n      <table id=\"table01\">\n"
    
    # for category in b[movie]:
        # output_html += "        <tr>\n          <td id=\"table01\" <div id=\"link-category\"> {{ 0 }} </div> </td>>\n".format(category.upper())
        # output_html += "          <td id=\"table01\">\n"
        
        # for link in b[movie][category]: 
            # output_html += "            <a href={0}> {1} </a>     \n".format(link, b[movie][category][link]['src'])
        
        # output_html += "          </td>\n        </tr>"
        
    # output_html += "      </table>\n    </td>\n  </tr>\n"

# output_html += "</table>" 

display = buildOP.buildDisplay(b) 
display_file= open("templates/display.html","w")
display_file.write(display)
display_file.close()


@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main2.html'))
        
    if flask.request.method == 'POST':
        return flask.render_template('display.html')

if __name__ == '__main__':
    app.run()