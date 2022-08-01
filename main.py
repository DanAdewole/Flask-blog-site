from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

post_objects = []

blog_url = "https://api.npoint.io/e3945d59591dd324411e"
response = requests.get(blog_url)
all_posts = response.json()

for blog_post in all_posts:
	post = Post(id=blog_post['id'], title=blog_post['title'], subtitle=blog_post['subtitle'], detail=blog_post['detail'])
	post_objects.append(post)


@app.route('/')
# @app.route('/index')
def home_page():
	return render_template("index.html", posts=post_objects)


@app.route('/about')
def about_page():
	return render_template("about.html")


@app.route('/contact')
def contact_page():
	return render_template("contact.html")


@app.route('/post/<int:id>')
def post_page(id):
	post_to_render = None
	for post in post_objects:
		if post.id == id:
			post_to_render = post
	print(post_to_render)
	return render_template("post.html", post=post_to_render)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

