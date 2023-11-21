from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")

def home():
    return render_template("a.html")

if __name__ == "__main__":
    app.run(debug=True)

# - Create Flask application instance with name 'app'
# - Pass it the variable __name__
# app = Flask(__name__) 

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return render_template('a.html')

# @app.route("/getimage")
# def get_img():
#     return "a.jpg"


# if __name__ == '__main__':
#     app.run()