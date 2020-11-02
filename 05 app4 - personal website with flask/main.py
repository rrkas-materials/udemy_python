# importing Flask
from flask import Flask
# for rendering html templates
from flask import render_template

# creates the app
app = Flask(__name__)


# '/' is for home by default
# other routes can be named as '/about'
@app.route('/')
def home_builder():
    return render_template('home.html')


@app.route('/about')
def about_builder():
    return render_template('about.html')


# start point
if __name__ == "__main__":
    app.run(debug=True)
