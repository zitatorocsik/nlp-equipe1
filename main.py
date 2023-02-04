from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
# def hello_world():
#    return render_template('index.html')

def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       uprompt = request.form.get("prompt")
       return "Your prompt is "+uprompt
    return render_template("index.html")

if __name__ == '__main__':
   app.run()