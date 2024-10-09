# This appallows you to create a username, password and asks you to login with it

# create username and password
print("hello user, create your name")
username = input()
print("Awesome! now create a password")
password = input()

# Login with the username and password created
print("...................................................................")
print("you have successfully signed up. please login with your credentials")
print("...................................................................")
userlogin = input("enter username here >>:")
# if userlogin == username:
#     print("nice one!")
#     userpassword = input("enter password: ")
#     if userpassword == password:
#         print("Access Granted!")
#     else:
#         print("wrong password. try again")
# else:
#     print("wrong user name.. try again")

while userlogin != username:
    print("wrong username, please try again")
    userlogin=input()
userpassword = input("please enter your password: ")
while userpassword != password:
    print("wrong password plaese try again: ")
    userpassword = input()
print(f"nice work,{username}. Access granted!")