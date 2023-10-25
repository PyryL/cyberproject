import hashlib
from werkzeug.security import check_password_hash, generate_password_hash

def generate_hash(string: str) -> str:
    # INTENTIONAL VULNERABILITY
    # Hash algorithm MD5 is broken and should not be used in storing passwords
    return hashlib.md5(string.encode("utf-8")).hexdigest()
    # FIX (comment the line above and uncomment the code below)
    # return generate_password_hash(string)

def check_hash(string: str, hash: str) -> bool:
    # INTENTIONAL VULNERABILITY CONTINUES
    # change this according to vulnerability in `generate_hash` function
    return generate_hash(string) == hash
    # FIX
    # return check_password_hash(hash, string)
