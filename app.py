from flask import Flask,jsonify
from scrape import data_collection





app = Flask(__name__)


@app.route("/<name>",methods = ["GET"])
def get_name(name):
    return f"Hello {name}"

@app.route("/",methods = ["GET"])
def get_data():
    return jsonify(data_collection())


if __name__ == "__main__":
    app.run()