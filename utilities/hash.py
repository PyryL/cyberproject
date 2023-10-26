import hashlib
from werkzeug.security import check_password_hash, generate_password_hash

def generate_hash(string: str) -> str:
    # INTENTIONAL VULNERABILITY
    # after enabling/disabling this vulnerability, run `setup_db.py` to reset the database
    # MD5 hash algorithm is broken and should not be used in storing passwords
    return hashlib.md5(string.encode("utf-8")).hexdigest()
    # FIX (comment the line above and uncomment the line below)
    # return generate_password_hash(string)

def check_hash(string: str, hash: str) -> bool:
    # INTENTIONAL VULNERABILITY CONTINUES
    # (change this according to vulnerability in `generate_hash` function above)
    return generate_hash(string) == hash
    # FIX (uncomment the code line below and comment the vulnerable line above)
    # (enable this fix only if the fix in `generate_hash` function has also been enabled)
    # return check_password_hash(hash, string)
