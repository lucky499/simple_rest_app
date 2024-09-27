from connexion import NoContent
import message

def health_check():
    """ to check health status"""
    return NoContent, 200

def greet_call():
    """ This is to say hi """
    message.greet()
    