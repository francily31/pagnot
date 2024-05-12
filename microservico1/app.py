from flask import Flask, request, jsonify
import pika
import requests

app = Flask(__name__)

@app.route('/pagar', methods=["POST"])
def pagar():
   data = request.json

   url = 'https://localhost:5001/notificar'

   x = requests.post(url, json = data)
   
   return jsonify({'status': 'enviado', 'response': x}), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)