from connexion import NoContent

def health_check():
    """ to check health status"""
    return NoContent, 200