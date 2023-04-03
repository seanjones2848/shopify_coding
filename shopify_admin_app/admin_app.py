from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>This is the Home Page.</p>"

@app.route("/shopify-auth-callback")
def shopify_auth_callback():
    return "<p>This is my Shopify Auth Callback Page</p>"

external_ip = requests.get("https://api.ipify.org/?format=json").json()
