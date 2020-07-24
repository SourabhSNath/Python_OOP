import hashlib
import os
os.system("clear")  # Just to clear the terminal each time it is run


class User:

    def __init__(self, username=None, password=None):
        self._username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        password = password.encode('utf-8')
        return hashlib.sha512(password).hexdigest()

    def check_password(self, password):
        password = self._encrypt_password(password)
        return password == self.password

    """
    @property and @username.setter are used to create
    getters and setters. They are used as if it were a property.
    
    print(user.username)
    username is coming from the getters and setters.
    _username is the variable, seen as a private variable.
    """
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        # Throwing an exception
        if not username:
            raise Exception("Username cannot be empty")
        else:
            self._username = username

    # Informal to String
    def __str__(self):
        return f"{self.username} \n {self.password}"

    # Formal to String
    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    # Check if username already exists
    def __eq__(self, other):
        return self.username == other.username


# user = User("Sourabh", "SSN")
# print(user.password)
# print(user.check_password("SSN"))

# user1 = User("Sourabh", "SSN")
# print(user == user1)

# print(user.username)

# user2 = User(password="SSN")
# user2.username = "Sourabh"
# print(f"User2 {user2}")
