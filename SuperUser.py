from User import User

# Inheritance, extending the User class
class SuperUser(User):
    
    def __init__(self, username, password, role):
        self.role = role
        super().__init__(username, password)

    def __str__(self):
        return super().__str__() + f"\n {self.role}"