from flask import Flask, render_template, request, jsonify
from chat import get_response
import time
app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("chatbot.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #check if text is valid
    response = get_response(text)
    message = {"answer": response }
    return jsonify(message)
    
@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

  
if __name__ == "__main__":
    app.run(debug=True)