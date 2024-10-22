# This app displays which student is most and least social and states their numbar of friends.

myclass ={}
myclass['john']={'age':19,'email':'johnny234@gmail.com','gender':'M','friends':['solomon','omolola','james']}
myclass['rachel']={'age':29,'email':'rachelgrace@gmail.com','gender':'F','friends':['YNW Melly','YNW Bslime']}
myclass['uche']={'age':19,'email':'uchechime@yahoo.com','gender':'M','friends':['old taker','new taker']}
myclass['emma']={'age':29,'email':'mannyeze@gmail.com','gender':'F','friends':[]}

# set variable for collating most or least friends
max = 100
min = 0

# loop through the dictionary

for key in myclass:
    user = myclass[key] # get each user's attributes
    friendslist = user['friends'] # get user's friends list 
    if len(friendslist) < max:
        least_social = key
        max = len(friendslist)
    if len(friendslist) > min:
        most_social = key
        min = len(friendslist)
print(f"{least_social} is the least sociable person in the class. Number of friends: {max} \n  {most_social} is the most sociable person with {min} friends")