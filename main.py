from flask import Flask, render_template

app = Flask(__name__)

# Codigo para la Landing Page
@app.route('/')
def hello():
    return render_template('index.html')

# Codigo para la pagina AboutHAMOC
@app.route('/about')
def about_page():
    return render_template('about.html')
