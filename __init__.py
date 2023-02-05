from flask import Flask, render_template

app = Flask(__name__)
type_of_cohere_model = ["xlarge-smart", "romantic", "test"]

@app.route("/")
def prompt():
    return render_template('base.html.j2', title="Hacku", models=type_of_cohere_model)

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