from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    fp = open('/etc/hostname', 'r')
    line = "Hello World!!! @" + fp.read()
    fp.close()
    return line

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
