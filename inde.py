from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)


@app.route('/refresh/', methods=['GET'])
def respond():


    # Retrieve the name from url parameter
    #name = request.args.get("refresh", None)
    response = {}
    response["MESSAGE"] = initialize()

    return jsonify(response)

@app.route('/')
def index():
    return "Welcome to my json server, if you want to get the data, please use refresh url"


def initialize():
    #GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    #CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    
    driver = webdriver.PhantomJS()
    user_name = "francis.rousseau32@gmail.com"
    password = "Louise999"
    driver.get("https://www.facebook.com")
    element = driver.find_element_by_id("email")
    element.send_keys(user_name)
    element = driver.find_element_by_id("pass")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    print(driver.title)
    return driver.title




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=4000)
