def get_random_password(n) -> str:
    import random
    import string
    password = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.sample(password, n))
print(get_random_password(8))
