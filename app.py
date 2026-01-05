from flask import Flask,jsonify,render_template
import requests

app=Flask(__name__)

@app.route('/')
def home():
    response=requests.get("http://127.0.0.1:8000/items/")
    data=response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)