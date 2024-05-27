import random
import string

def generate_random_id(district_code, length=6):
    random_string = ''.join(random.choices(string.digits, k=length))
    random_id = f"{district_code}{random_string}"
    return random_id
