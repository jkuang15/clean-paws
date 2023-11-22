from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def landing():
  return render_template("home.html")

@app.route("/bin_capacity")
def bin_capacity():
  return render_template("bin_capacity.html")

@app.route("/")
def hardware_names():
  names = ['Miguel Murillo', 'Wilson Nguyen', 'Ellen So', 'Arim Song']
  return render_template('home.html', names=names)

# @app.route("/")
# def software_names():
#   names = ['Elise Ji', 'Jamie Kuang', 'Steven Lee', 'Natalie Perrochon']
#   return render_template('home.html', names=names)

if __name__ == "__main__":
  app.run(debug=True)

