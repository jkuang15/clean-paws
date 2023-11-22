from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
  return render_template("home.html")

@app.route("/bin_capacity")
def bin_capacity():
  return render_template("bin_capacity.html")

if __name__ == "__main__":
  app.run(debug=True)

