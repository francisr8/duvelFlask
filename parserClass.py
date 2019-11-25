from webbot import Browser
from selenium.webdriver.support.ui import Select
web = Browser()
print('JaHe@2019')

def initialize():
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
    goodValue = False

    while (not goodValue):
        returnedvalue = read()
        if returnedvalue == "Duvel Moortgat;Log Out;Home;Sales;Events;Guides;About;Login;Find;Next;;" or returnedvalue == "Duvel Moortgat;Log Out;Home;Sales;Events;Guides;About;Login;Vedett biervilten;Vedett bottle glorifier;Duvel biervilten;Vedett biervilten;Welkom op onze verni;read more;Learn more;Learn more;":
            goodValue = False
        else:
            goodValue = True

    return returnedvalue


def read():
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
