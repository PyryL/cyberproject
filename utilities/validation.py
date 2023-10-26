import re

class Validation:
    @classmethod
    def is_valid_username(cls, username: str) -> bool:
        return re.match("^[a-zA-Z0-9_]{3,12}$", username) is not None

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        # check that password contains all wanted character categories
        # list contains False if password does not meet the criterion
        criteria = [
            re.search("[0-9]", password) is not None,     # contains a digit
            re.search("[a-z]", password) is not None,     # contains a lowercase character
            re.search("[A-Z]", password) is not None,     # contains an uppercase character
            re.search("[^0-9a-zA-Z]", password) is not None,     # contains a character that is none of previous
        ]
        if False in criteria or len(password) < 8:
            return False

        # check if the password is in a dictionary list
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                if password == line.strip():
                    return False
        
        return True

    @classmethod
    def is_valid_todo_content(cls, content: str) -> bool:
        return len(content.strip()) != 0
