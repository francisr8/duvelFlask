from flask import Flask, request, jsonify
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
    web.get('http://sales.duvel.com/Account/Login.aspx')
    web.find_element_by_id('MainContent_LoginUser_UserName').send_keys('jana')
    web.find_element_by_id('MainContent_LoginUser_Password').send_keys('Hermans25')
    web.find_element_by_id('MainContent_LoginUser_LoginButton').click()
    web.find_element(By.XPATH, "/html/body/div[1]/div[1]/form/ul/li[4]/a").click()
    web.find_element_by_id('LoginView_lnkPlanning').click()
    web.find_element_by_id('ctl00_MainContent_ReportViewer1_ctl04_ctl03_ddValue').click()
    select = Select(web.find_element_by_id("ctl00_MainContent_ReportViewer1_ctl04_ctl03_ddValue"))
    select.select_by_value('2')
    web.find_element_by_id('ctl00_MainContent_ReportViewer1_ctl04_ctl00').click()
    web.implicitly_wait(1)
    element = web.find_element(By.XPATH,
                               "/html/body/div/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]")
    return element.text.replace("\n", ";").replace("  ", ";") + ";"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=4000)
