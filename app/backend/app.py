import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Juan",
        "lastname": "Gomez",
        "socialMedia":
        [
            {"facebookUser": "MY_FACEBOOK_USER"},
            {"instagramUser": "MY_INSTAGRAM_USER"},
            {"xUser": "MY_X_USER"},
            {"linkedin": "MY_LINKEDIN_USER"},
            {"githubUser": "MY_GITHUB_USER"}
        ],
        "blog": "https://juangomezb.com",
        "author": "Juan Gomez"
    }
    return json.dumps(value)