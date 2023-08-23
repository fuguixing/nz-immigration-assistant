from flask import Flask, request, jsonify
from user import User
from ai_agent import AIAgent
from chat_interface import ChatInterface

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    """Endpoint to ask a question to the AI agent."""
    question = request.json['question']
    user = User(name="John Doe", email="johndoe@example.com", immigration_status="visitor", immigration_goal="permanent resident")
    ai_agent = AIAgent()
    chat_interface = ChatInterface(user, ai_agent)
    response = chat_interface.send_message(question)
    return jsonify(response)

@app.route('/plan', methods=['POST'])
def plan():
    """Endpoint to request an immigration plan from the AI agent."""
    user_data = request.json['user']
    user = User(name=user_data['name'], email=user_data['email'], immigration_status=user_data['immigration_status'], immigration_goal=user_data['immigration_goal'])
    ai_agent = AIAgent()
    chat_interface = ChatInterface(user, ai_agent)
    plan = chat_interface.receive_message()
    return jsonify(plan)

if __name__ == '__main__':
    app.run(debug=True)
