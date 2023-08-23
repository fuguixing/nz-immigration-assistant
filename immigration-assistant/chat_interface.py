from typing import Dict
from user import User
from ai_agent import AIAgent

class ChatInterface:
    """Class to handle user messages and display AI agent responses."""

    def __init__(self, user: User, ai_agent: AIAgent):
        """Initializes the ChatInterface class with a User object and an AIAgent object."""
        self.user = user
        self.ai_agent = ai_agent

    def send_message(self, message: str) -> Dict[str, str]:
        """Sends a message from the user to the AI agent and returns the AI agent's response."""
        response = self.ai_agent.answer_question(message)
        return {"user": message, "ai_agent": response}

    def receive_message(self) -> Dict[str, str]:
        """Receives a message from the AI agent and returns it."""
        return {"ai_agent": self.ai_agent.create_plan(self.user)["plan"]}
