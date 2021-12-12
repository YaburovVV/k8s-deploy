from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Зай :*</h1><h3>🚀 The first flight page!</h3> <br/> Try to GET and POST <a href='/emotion'>/emotion<a/>."


@app.route("/emotion", methods=['GET', 'POST'])
def emotion():
    if request.method == 'POST':
        hd = 'None'
        hd_name = 'Charset'
        if hd_name in request.headers:
            hd = request.headers[hd_name]
        data = request.get_data()
        return data
    else:
        return "This is GET request %) Just try POST. Use Postmen <br/>POST /emotion"
