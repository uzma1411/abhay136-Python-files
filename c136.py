
from flask import Flask,jsonify,request
from data import data
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

@app.route("/me")
def index2():
    return jsonify({
        "data":"ABhay's class",
        "message":"success"
    }),200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data,
        "message":"success"
    }),200



if __name__ == "__main__":
    app.run(port=5500,host="localhost",debug=True)