import string
import random
import hashlib
import time


CHARACHTERS = string.digits + string.ascii_letters + string.punctuation


def unique_slugify(txt):
    salt_length = random.randint(10, 70)
    salt = "".join(random.choices(CHARACHTERS)[0] for _ in range(salt_length))

    h = hashlib.md5()
    h.update((txt + salt + str(time.time())).encode())

    return h.hexdigest()[:8]