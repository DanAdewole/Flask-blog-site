from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/e3945d59591dd324411e"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
# @app.route('/index')
def home_page():
	return render_template("index.html", posts=all_posts)


@app.route('/about')
def about_page():
	return render_template("about.html")


@app.route('/contact')
def contact_page():
	return render_template("contact.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

