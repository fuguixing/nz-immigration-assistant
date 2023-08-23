class User:
    """Class to represent a user who interacts with the AI agent."""

    def __init__(self, name: str, email: str, immigration_status: str, immigration_goal: str):
        """Initializes the User class with the user's name, email, immigration status, and immigration goal."""
        self.name = name
        self.email = email
        self.immigration_status = immigration_status
        self.immigration_goal = immigration_goal

    def get_immigration_plan(self, ai_agent) -> dict:
        """Requests a personalized immigration plan from the AI agent."""
        return ai_agent.create_plan(self)
