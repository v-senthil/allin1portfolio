from flask import Flask,render_template, request, make_response, Response, redirect, url_for, session
import requests
from flask_session import Session
from dotenv import load_dotenv
import os
import feedparser

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
load_dotenv()

@app.route("/")
def index():
	return render_template('index.html')

# GitHub
@app.route("/github", methods=['POST', 'GET'])
def github():
	if request.method == 'POST':
		gituser = request.form['gitusername']
		session["gituser"] = gituser
		url = "https://api.github.com/users/"+gituser+"/repos"
		headers = {'Authorization': os.getenv('GitHub')}
		response = requests.request("GET", url, headers=headers)
		userurl = "https://api.github.com/users/"+gituser
		userdatares =  requests.request("GET", userurl, headers=headers)
		if response.status_code != 200 and userdatares.status_code != 200:
			return render_template('error.html')
		else:
			posts = response.json()
			userdata = userdatares.json()
			lendata = len(posts)
		return render_template('github.html', gituser=gituser, posts=posts, userdata=userdata)
	else:
		return render_template('github.html', gituser="none")

#Github from url
@app.route("/profile/github/<name>")
def githuburl(name):
	url = "https://api.github.com/users/"+name+"/repos"
	headers = {'Authorization': os.getenv('GitHub')}
	response = requests.request("GET", url, headers=headers)
	userurl = "https://api.github.com/users/"+name
	userdatares =  requests.request("GET", userurl, headers=headers)
	if response.status_code != 200 and userdatares.status_code != 200:
		return render_template('error.html')
	else:
		posts = response.json()
		userdata = userdatares.json()
		lendata = len(posts)
		return render_template('github.html', gituser=name, posts=posts, userdata=userdata)

# Twitter
@app.route("/twitter")
def twitter():
	return render_template('twitter.html')

# Dev.to
@app.route("/devto",methods=['POST', 'GET'])
def devto():
	if request.method == 'POST':
		devtouser = request.form['devtousername']
		session["devtouser"] = devtouser
		url = "https://dev.to/api/articles?username="+devtouser
		headers = {'api-key': os.getenv("Dev_To")}
		response = requests.request("GET", url, headers=headers)
		userurl = "https://dev.to/api/users/by_username?url="+devtouser
		userdatares =  requests.request("GET", userurl, headers=headers)
		if len(response.text) < 5 and len(userdatares.text) < 5:
			return render_template('error.html')
		else:
			posts = response.json()
			userdata = userdatares.json()
			lendata = len(posts)
		return render_template('devto.html', devtouser=devtouser, posts=posts, userdata=userdata)
	else:
		return render_template('devto.html', devuser="none")

#Dev.to from url
@app.route("/profile/devto/<name>")
def devtourl(name):
	url = "https://dev.to/api/articles?username="+name
	headers = {'api-key': 'DweJQwcBMRd9uFxFAA2Yh4hn'}
	response = requests.request("GET", url, headers=headers)
	userurl = "https://dev.to/api/users/by_username?url="+name
	userdatares =  requests.request("GET", userurl, headers=headers)
	if len(response.text) == 2:
		return render_template('error.html')
	else:
		posts = response.json()
		userdata = userdatares.json()
		lendata = len(posts)
		return render_template('devto.html', devuser=name, posts=posts, userdata=userdata)

# Medium
@app.route("/medium", methods=["POST", "GET"])
def medium():
	if request.method == 'POST':
		mediumuser = request.form['mediumuser']
		session["mediumuser"] = mediumuser
		rss_url = "https://medium.com/feed/@"+mediumuser
		urldata = feedparser.parse(rss_url)
		if len(urldata["entries"]) <= 0:
			return render_template('error.html')
		else:
			data = urldata["entries"]
			return render_template('medium.html', name=mediumuser, data=data)
	else:
		return render_template('medium.html', name="none")

#Medium from url
@app.route("/profile/medium/<name>")
def mediumurl(name):
	rss_url = "https://medium.com/feed/@"+name
	urldata = feedparser.parse(rss_url)
	if len(urldata["entries"]) <= 0:
		return render_template('error.html')
	else:
		data = urldata["entries"]
		return render_template('medium.html', name=name, data=data)


# Facebook

# Error Page
@app.route("/eror")
def error():
    return render_template('error.html')








if __name__ == "__main__":
    app.run(debug=True,port=3000)
