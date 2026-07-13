print("===============Password Limit Attemts===============")

password = "python@123=aai"
attempts = 0

while attempts < 3:
    user_password = input("Enter your password:-")

    if password == user_password:
        print("Logged in successful")
        break
    else:
        print("Please enter correct password")
    attempts += 1

if attempts == 3:
    print("account locked")