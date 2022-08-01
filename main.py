from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
# @app.route('/index')
def home_page():
	return render_template("index.html")


@app.route('/about')
def about_page():
	return render_template("about.html")


@app.route('/contact')
def contact_page():
	return render_template("contact.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

