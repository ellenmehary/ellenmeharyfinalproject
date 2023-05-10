from flask import Flask, render_template, request
import pysolr
import os

# Connect to Solr
solr_url = 'http://localhost:8983/solr/new_core/select/?q=*'

solr = pysolr.Solr(solr_url, always_commit=True)

# Create the Flask app instance and set the template folder
app = Flask(__name__, template_folder='/Users/ellenmehary/ellenmeharyfinalproject/templates')

@app.route('/')
def home():
    return render_template('home.html')

# Search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    if query:
        # Print query string
        print(f"Query string: {query}")
        
        # Search Solr
        results = solr.search(query)
        print(results)
        return render_template('search.html', results=results)
    else:
        return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)

