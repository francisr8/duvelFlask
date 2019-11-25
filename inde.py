from flask import Flask, request, jsonify
#from webbot import Browser
app = Flask(__name__)
#web = Browser()


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



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
