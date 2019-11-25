from flask import Flask, request, jsonify
from webbot import Browser
app = Flask(__name__)
web = Browser()


@app.route('/refresh/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    #name = request.args.get("refresh", None)
    response = {}
    response["MESSAGE"] = "IDK"

    return jsonify(response)

@app.route('/')
def index():
    return "Welcome to my json server, if you want to get the data, please use refresh url"


def initialize():
    try:
        goodValue = False

        while (not goodValue):
            returnedvalue = read()
            if returnedvalue == "Duvel Moortgat;Log Out;Home;Sales;Events;Guides;About;Login;Find;Next;;" or returnedvalue == "Duvel Moortgat;Log Out;Home;Sales;Events;Guides;About;Login;Vedett biervilten;Vedett bottle glorifier;Duvel biervilten;Vedett biervilten;Welkom op onze verni;read more;Learn more;Learn more;":
                goodValue = False
            else:
                goodValue = True

        return returnedvalue
    except:
        print("Error")
        return "Er is een fout gebeurd"


def read():
    web.go_to('http://sales.duvel.com/Account/Login.aspx')
    web.type('jana', into='email', id='loginName')
    web.click('NEXT', tag='span')
    test = "Hermans25"
    web.type(test, into='password', id='password')
    web.click('Log in', multiple=False)
    web.click('Guides', multiple=False)
    web.click('Planning', multiple=False)
    web.click(id='ctl00_MainContent_ReportViewer1_ctl04_ctl03_ddValue')
    web.click("Duvel", tag='option')
    web.click("View Report")

    data = 4
    list = []
    textT = ''

    for i in range(5):
        element = web.find_elements(
            xpath='/html/body/div/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[' + str(
                data + i) + ']')
        for i in element:
            if i.text.replace("\n", "") == "  ":
                textT += ";"
            else:
                textT += i.text.replace("\n", ";").replace("  ", ";") + ";"
        print(textT)
        list.append(textT)
        textT = ''
    return list



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
