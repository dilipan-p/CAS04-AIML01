from flask import Flask, request, jsonify
import openai
from pymongo import MongoClient

app = Flask(__name__)
# openai.api_key =""
client=MongoClient("mongodb://localhost:27017/")
db=client("ecommerce")
orders_collection=db["orders"]
@app.route('/chat',methods=['POST'])
def chat():
    user_input=request.json['message']
    response=openai.ChatCompletion.create(
        model="gpt-4",messages=[{"role":"user","content":user_input}]
    )

    return jsonify({"response":response['choices'][0]['message']['content']})

@app.route('/order_status'methods=['GET'])

def order_status():

    return "hello"

