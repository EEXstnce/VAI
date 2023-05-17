from flask import Flask, render_template, request, jsonify
from app import ChatSession

app = Flask(__name__)
chat_session = ChatSession()


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/message', methods=['POST'])
def message():
  message = request.json['message']
  response = chat_session.run_chain(message)
  return jsonify(response=response)


if __name__ == "__main__":
  app.run(debug=True)
