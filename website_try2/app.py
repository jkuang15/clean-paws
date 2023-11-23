from flask import Flask, render_template
import photo_handler as ph

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("home.html")

@app.route("/bin_capacity")
def bin_capacity():
    photos = ph.get_all_photos()
    return render_template("bin_capacity.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)

