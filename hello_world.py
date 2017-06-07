from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
        Here's a picture of a kitten. Aww...Here
        </p>
        <img src="http://placekitten.com.s3.amazonaws.com/homepage-samples/200/138.jpg">
        
    """
    return html.format(name.title())

@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
    
    first_name = firstname[:2]
    last_name = lastname[:3]
    
    jedi = str(last_name + first_name)
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
        Here's a picture of a kitten. Aww...Here
        </p>
        <img src="http://placekitten.com.s3.amazonaws.com/homepage-samples/200/138.jpg">
        
    """
    return html.format(jedi.title())

    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            