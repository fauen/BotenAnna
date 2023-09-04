import random

def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '/roll':
        return str(random.randint(1, 6))
    
    if p_message == 'welcome':
        return 'Welcome to the server!'

    if p_message == '!help':
        return "Currently I can't do much but I'm learning. You can use `/roll` to roll a dice though."