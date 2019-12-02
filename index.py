from flask import Flask, request, jsonify
import os
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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://www.google.com")
    print(driver.page_source)



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=4000)
