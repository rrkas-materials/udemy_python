from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id_ = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route('/')
def index_builder():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success_builder():
    if request.method == 'POST':
        email = request.form['email']
        height = request.form['height']

    return render_template('success.html')

# if __name__ == '__main__':
#     app.debug = True
#     app.run(port=5001)
