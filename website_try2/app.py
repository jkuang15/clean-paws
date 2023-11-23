from flask import Flask, render_template
import photo_handler as ph


app = Flask(__name__)

@app.route("/")
def landing():
    hardware_names = ['Miguel Murillo', 'Wilson Nguyen', 'Ellen So', 'Arim Song']
    software_names = ['Elise Ji', 'Jamie Kuang', 'Steven Lee', 'Natalie Perrochon']
    return render_template("home.html", hardware_names = hardware_names, software_names = software_names)

@app.route("/bin_capacity")
def bin_capacity():
    photos = ph.get_all_photos()
    return render_template("bin_capacity.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)

