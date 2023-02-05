# nlp-equipe1
~~This branch isn't meant to see the light of day and meant has a demo for the tool we're using. ty~~
This branch will  end up seeing the light of day.

## Dependencies
- cohere
- flask>=2.0

## How to run in localhost
- set flask app env
```
set FLASK_APP=__init__.py
```
- launch the app in localhost
```
flask run
```

## Warning
While it can be similar to python, jinja templates have their own syntax and fonction. For example, the `len(var_here)` function isn't a thing, instead it's `var_here|length` (very cursed).