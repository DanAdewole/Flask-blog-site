from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

post_objects = []
my_email = os.getenv("my_email")
password = os.getenv("password")
receiving_mail = os.getenv("receiving_email")
print(receiving_mail)

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


@app.route('/contact', methods=["POST", "GET"])
def contact_page():
	if request.method == 'POST':
		name = request.form['username']
		email = request.form['email']
		phone_number = request.form['phone_number']
		message = request.form['message']
		msg_body = f"Subject: New Message!\n\nName: {name} \nEmail: {email} \nPhone Number: {phone_number} \nMessage: {message}"
		print(msg_body)
		print(receiving_mail)

		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
			# connection.starttls()
			connection.ehlo()
			connection.login(user=my_email, password=password)
			connection.sendmail(
                from_addr=my_email,
                to_addrs=receiving_mail,
                msg=msg_body
            )

		return render_template("contact.html", method="POST")
	else:
		return render_template("contact.html", method="GET")


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

