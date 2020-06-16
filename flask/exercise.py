# Set up your imports here!
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome!</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    if name[-1]=='y':
        pupname = name[:-1] + 'iful'
        
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    else:
        pupname = name + 'y'
    
    return f'<h1> Your pupname is {pupname}'

if __name__ == '__main__':
    # Fill me in!
      app.run(debug=True)