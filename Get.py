from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
cred_url = "mongodb+srv://Diligent:Diligent1234@cluster0.1pnpt.mongodb.net/?retryWrites=true&w=majority"
cred = MongoClient(cred_url)

db = cred["MyDatabase"]
collection = db["UserID"]

@app.route("/")
def home():
    return ""

@app.route("/<mobile>")
def search(mobile):
    res = collection.find_one({"Contact_No":f"{mobile}"})
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)
