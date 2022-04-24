class UserAlreadyExists(Exception):
    def __init__(self):
        self.message = 'User with the same email already exists'
        super().__init__(self.message)
