from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)


@app.route('/refresh/', methods=['GET'])
def respond():
    response = {}
    response["MESSAGE"] = initialize()
    return jsonify(response)

@app.route('/')
def index():
    return "Welcome to my json server, if you want to get the data, please use refresh url"


def initialize():
    browser = webdriver.Chrome()
    browser.get("http://www.facebook.com")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    submit = browser.find_element_by_id("loginbutton")
    username.send_keys("test")
    password.send_keys("test")
    submit.click()




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=4000)
