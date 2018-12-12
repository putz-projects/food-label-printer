"""A file to manage users, and produce lolcodes.
"""

import os
import json
import hashlib

def get_key(key, default=None):
    rv = default

    if not os.path.exists("users.json"):
        return rv

    with open("users.json", "r") as f:
        j = json.loads(f.read())
        if key in j:
            rv = j[key]
    return rv

def set_key(key, value):
    if not os.path.exists("users.json"):
        j = {}
        j[key] = value
    else:
        with open("users.json", "r") as f:
            j = json.loads(f.read())
            j[key] = value

    with open("users.json", "w") as f:
        f.write(json.dumps(j))

def value_exists(value):
    if not os.path.exists("users.json"):
        return False

    with open("users.json", "r") as f:
        j = json.loads(f.read())
        for k, v in j.items():
            if value == v:
                return True
    return False

def get_hash(s):
    m = hashlib.sha256()
    m.update(s.encode())
    return str(m.hexdigest())

def get_lolcode(code):
    h = get_hash(code)

    if get_key(code):
        return get_key(code)

    current_index = 1
    current_guess = h[:current_index]
    while value_exists(current_guess):
        current_index += 1
        current_guess = h[:current_index]

    set_key(code, current_guess)
    return current_guess

def get_kerb(lolcode):
    return get_key(lolcode)

def set_kerb(lolcode, kerb):
    set_key(lolcode, kerb)
