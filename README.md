# Cyber Security Base - Project I

Project for [Cyber Security Base](https://cybersecuritybase.mooc.fi/module-3.1) course at the University of Helsinki in autumn 2023. This project intentionally contains vulnerabilities and fixes to them.

## Installation

Use Python version 3.8 or later.

Install Python dependencies by running

```
pip install -r requirements.txt
```

Create a file called `.env` and set its content as follows:

```
SECRET_KEY=abcabcabcabcabcabcabcabcabcabcab
```

Replace the `abc` part with a random secret string.

Format and prepare database by running

```
python setup_db.py
```

(depending on your configuration you may need to replace `python` with `python3`)

## Usage

Start local server by running

```
flask run
```

After making changes to the code (e.g. un/commenting code related to vulnerabilities) stop and restart the server.

Some vulnerabilities also require database reset after being enabled or disabled. In these cases run `setup_db.py` script before restarting the server.

## Sources

OWASP top-10 [vulnerability list](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication.html) version 2017 has been used as a reference.

`passwords.txt` is a list of easy-to-guess passwords. It has been made by combining [this](https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords-1000000.txt) and [this](https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkweb2017-top10000.txt) password list and filtering out passwords that do not meet other criteria of the application. Both of the mentioned lists are released under MIT license.
