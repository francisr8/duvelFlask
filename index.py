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
    web = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    web.go_to('http://sales.duvel.com/Account/Login.aspx')
    web.type('jana', into='email', id='loginName')
    web.click('NEXT', tag='span')
    test = "Hermans25"
    web.type(test, into='password', id='password')
    web.click('Log in', multiple=False)
    web.click('Guides', multiple=False)
    web.click('Planning', multiple=False)
    web.click(id='ctl00_MainContent_ReportViewer1_ctl04_ctl03_ddValue')
    print(web.exists('Achouffe'))
    web.click("Duvel", tag='option')
    web.click("View Report")
    textT = ""
    element = web.find_elements(xpath='/html/body/div/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[' + str(5) + ']')
    for i in element:
        if i.text.replace("\n", "") == "  ":
            textT += ";"
        else:
            textT += i.text.replace("\n", ";").replace("  ", ";") + ";"
    return textT



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=4000)
