from flask import Flask, render_template

app = Flask(__name__)
type_of_cohere_model = ["xlarge-smart", "romantic", "test"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><br/><a href=\"/home\">link to home page</a>"

@app.get("/home")
def prompt():
    return render_template('base.html.j2', title="custom title wow", models=type_of_cohere_model)

@app.post("/<category>/<prompt>")
def generate(category=None, prompt=""):
    """
    Parameters
    ----------
    category : str
        which model to use
    prompt : str
        input for model
    Returns
    -------
    output : str
        output from selected model TODO
    """
    output = "TODO"
    return "prompt is " + prompt + ", output is " + output