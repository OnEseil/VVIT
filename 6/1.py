class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

account = UserAccount('name', 'pass')
print(account.username, account.check_password('pass'))

account.set_password('new_pass')
print(account.check_password('pass'))
print(account.check_password('new_pass'))
