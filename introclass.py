#This app asks you your name,age and tell you your age in 1 year's time

# step one - greet the user and ask their name
print("welcome, please what is your name?")
username = input()

# step two, greet the user by name and ask for their age
print("HELLO",username,"How old are you?")
userage = input()

# step three, tell the user their age next year
if userage < 18:
    print(f"dear{username} you are a minor. you will be",userage+1,"years old next year")
elif userage <=30:
    print(f"dear {username} you are a young adult. you will be", userage+1,"years old next year")
elif userage <=45:
    print(f"dear{username}you are middle-age. you will be",userage+1,"years old next year")
elif userage <= 75:
    print(f"dear{username}you are getting old. you will be",userage+1,"years old next year")
else:
    print(f"dear{username}you are quite old. you will be",userage+1,"years old next year")