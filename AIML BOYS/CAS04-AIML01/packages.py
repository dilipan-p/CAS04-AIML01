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
        model="gpt-3.5",messages=[{"role":"user","content":user_input}]
    )

    return jsonify({"response":response['choices'][0]['message']['content']})

@app.route('/order_status',methods=['GET'])

def order_status():
    order_id=request.args.get('order_id')
    order=orders_collection.find_one({"order_id":order_id})

    if order:
         return jsonify({"status":order["status"]})
    else:
         return jsonify({"error":"Order not found"}),404
    
if __name__== '__main__':
     app.run(debug=True)
    

