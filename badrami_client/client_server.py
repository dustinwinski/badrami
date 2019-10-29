from flask import Flask,render_template,request, redirect, url_for, flash, make_response


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)