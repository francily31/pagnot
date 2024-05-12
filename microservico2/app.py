from flask import Flask, request, jsonify
import pika
import requests

app = Flask(__name__)

@app.route('/notificar', methods=["POST"])
def pagar():
    data = request.json
   
    # mandar para o rabbit mq o data

    return jsonify({'status': 'enviado'}), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)