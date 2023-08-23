## Required Python third-party packages
```python
"""
flask==1.1.2
bcrypt==3.2.0
openai==0.27.0
"""
```

## Required Other language third-party packages
```python
"""
No third-party packages in other languages are required.
"""
```

## Full API spec
```python
"""
openapi: 3.0.0
info:
  title: NZ Immigration AI API
  version: 1.0.0
paths:
  /ask:
    post:
      summary: Ask a question
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                question:
                  type: string
      responses:
        '200':
          description: The answer to the question
          content:
            application/json:
              schema:
                type: object
                properties:
                  answer:
                    type: string
  /plan:
    post:
      summary: Request an immigration plan
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user:
                  $ref: '#/components/schemas/User'
      responses:
        '200':
          description: The immigration plan
          content:
            application/json:
              schema:
                type: object
                properties:
                  plan:
                    type: string
components:
  schemas:
    User:
      type: object
      properties:
        name:
          type: string
        email:
          type: string
        immigration_status:
          type: string
        immigration_goal:
          type: string
"""
```

## Logic Analysis
```python
[
    ("main.py", "Contains the main entry point of the application. Initializes the Flask app and the AI agent."),
    ("ai_agent.py", "Contains the AI agent class. This class is responsible for answering questions and creating immigration plans."),
    ("chat_interface.py", "Contains the chat interface class. This class is responsible for handling user messages and displaying AI agent responses."),
    ("immigration_data.py", "Contains the immigration data class. This class is responsible for providing the AI agent with up-to-date immigration information."),
    ("user.py", "Contains the user class. This class is responsible for storing user information and interacting with the AI agent.")
]
```

## Task list
```python
[
    "immigration_data.py",
    "ai_agent.py",
    "user.py",
    "chat_interface.py",
    "main.py"
]
```

## Shared Knowledge
```python
"""
'immigration_data.py' contains the ImmigrationData class, which provides the AI agent with up-to-date immigration information. It should be implemented first as it is a dependency for the AI agent.

'ai_agent.py' contains the AIAgent class, which uses the GPT-3 model to answer questions and create immigration plans. It depends on the ImmigrationData class.

'user.py' contains the User class, which stores user information and interacts with the AI agent. It does not have any dependencies and can be implemented in parallel with the AI agent.

'chat_interface.py' contains the ChatInterface class, which handles user messages and displays AI agent responses. It depends on the User and AIAgent classes.

'main.py' contains the main entry point of the application. It initializes the Flask app and the AI agent. It depends on all other classes and should be implemented last.
"""
```

## Anything UNCLEAR
The requirement is clear to me.