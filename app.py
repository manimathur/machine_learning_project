from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["GET","POst"])
def index():
    return "First Project"



if __name__ == '__main__':
    app.run(debug=True)