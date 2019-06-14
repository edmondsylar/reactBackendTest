import random
import string
from flask import jsonify


def randomStringDigits(stringLength=9):

    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_uppercase + string.digits
    code =  (''.join(random.choice(lettersAndDigits) for i in range(stringLength)))
    return (code)