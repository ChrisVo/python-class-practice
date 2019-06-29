class Email:
    def __init__(self):
        self.is_set = False

    def send_email(self):
        self.is_set = True


my_email = Email()
print(my_email.is_set)

my_email.send_email()

print(my_email.is_set)
