# 🤔: Gabriel Thompson, Emily Ortiz
# SoftDev
# K20: A RESTful Journey Skyward
# 2022-11-22
# time spent: 0.7 hrs

from flask import Flask, render_template
import requests

app = Flask(__name__)

key = open("key_nasa.txt", "r").read() #key is string
key = key.strip() #removing white space

@app.route("/")
def index():
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={key}" # url with api key
    web = requests.get(api_url).json() #json data of api_url, web is a dictionary
    img_url = web["url"] #gets url of img from web dictionary
    img_title = web["title"]
    img_explanation = web["explanation"]
    return render_template("main.html", title=img_title, explanation=img_explanation, url=img_url)

if __name__ == "__main__":
    app.debug = True
    app.run()
