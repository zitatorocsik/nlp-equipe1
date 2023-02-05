from flask import Flask, render_template
import cohere
# This is your trial API key
co = cohere.Client('zSkJ2OBgt7odMEb8Hg2u9LZkdpnNkW8pv3t3C5SI')


app = Flask(__name__)
type_of_cohere_model = ["xlarge-smart", "romantic", "test"]


@app.route("/")
def prompt():
    return render_template('base.html.j2', title="Hacku", models=type_of_cohere_model)


@app.post("/<category>/<prompt>")
def generate(category=None, prompt=""):
    base_prompt = """Write me a poem about: birds, sky
Haiku:
a skein of birds
twines across the sky
the northbound train departs

---
Write me a poem about: headlights, fade
Haiku:
morning commute-
headlights fade
in the whiteout

---
Write me a poem about: ferry
Haiku:
homebound ferry
thoughts zigzagging
with the terns

---
Write me a poem about: leaves
Haiku: 
yellow walnut leaves
slowly appear on the lawn
early morning light     

--- 
Write me a poem about: """

    while True:
        response = co.generate(
            model='medium',
            prompt=base_prompt + prompt.strip() + "\nHaiku:",
            max_tokens=75,
            temperature=0.4,
            stop_sequences=["---"],
            frequency_penalty=0.3
        )
        ai_haiku = 'Haiku: {}'.format(response.generations[0].text)

        count = -2
        for c in ai_haiku:
            if c == '\n':
                count = count + 1
        
        if count == 3:
            break

    ai_haiku_lines = ai_haiku.split('\n')
    ai_haiku_final = ai_haiku_lines[1] + "<br>" + \
        ai_haiku_lines[2] + "<br>" + ai_haiku_lines[3]

    output = ai_haiku_final
    return output
