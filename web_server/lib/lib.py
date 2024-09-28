from connexion import NoContent
from server_code import  message

def health_check():
    """ to check health status"""
    return NoContent, 200

def greet_call():
    """ This is to say hi """
    return message.greet(), 200
    
