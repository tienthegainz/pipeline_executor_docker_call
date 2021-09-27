import string
import random

def random_string(N: int = 7):
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))