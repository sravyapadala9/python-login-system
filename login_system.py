# Login System

username = "admin"
password = "12345"

print("===== Login System =====")

user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == username and pwd == password:
    print("Login Successful! Welcome,", user)
else:
    print("Invalid Username or Password!")