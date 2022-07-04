username, password = input('What is your username?'), input('What is your password?')
password_length = len(password)


print(f"{username}, your password {password.replace(password, ('*' * password_length))} is {password_length} characters long")