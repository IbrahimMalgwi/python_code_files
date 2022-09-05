users = [
    {'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'user_name': 'deezah',
     'is_verified': True,
     'tweet': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku fis our man', 'likes': 4, 'retweets': 2}
     ]
     },
    {'name': 'Ibrahim',
     'age': 32,
     'gender': 'Male',
     'user_name': 'ibro',
     'is_verified': False,
     'tweet': [
         {'content': 'Programming is fun', 'likes': 34, 'retweets': 10},
         {'content': 'Love python', 'likes': 5, 'retweets': 33}
     ]
     },
    {'name': 'James',
     'age': 25,
     'gender': 'Male',
     'user_name': 'amez',
     'is_verified': True,
     'tweet': [
         {'content': 'love is life', 'likes': 6, 'retweets': 89},
         {'content': 'only Rachael I know', 'likes': 97, 'retweets': 2}
     ]
     },
    {'name': 'Rachael',
     'age': 21,
     'gender': 'Female',
     'user_name': 'betty',
     'is_verified': False,
     'tweet': [
         {'content': '.', 'likes': 1450, 'retweets': 1330},
         {'content': 'Thinking about Amez', 'likes': 4, 'retweets': 2},
         {'content': 'Amezing grace', 'likes': 2000, 'retweets': 1542}
     ]
     },
    {'name': 'Elijah',
     'age': 17,
     'gender': 'Male',
     'user_name': 'el_d_si',
     'is_verified': False,
     'tweet': [
         {'content': '#Osun decides', 'likes': 12, 'retweets': 8},
         {'content': 'imole de', 'likes': 4, 'retweets': 2}
     ]
     },
    {'name': 'Dorris',
     'age': 16,
     'gender': 'Female',
     'user_name': 'anything',
     'is_verified': False,
     'tweet': [
         {'content': 'I love Chimamanda', 'likes': 450, 'retweets': 233},
         {'content': 'Feminism is the goal', 'likes': 4000, 'retweets': 2245}
     ]
     },
    {'name': 'Jacob',
     'age': 37,
     'gender': 'Male',
     'user_name': 'elder_j',
     'is_verified': True,
     'tweet': [
         {'content': 'Reflection is my goal', 'likes': 50, 'retweets': 3},
         {'content': 'How to get more likes on twitter', 'likes': 1, 'retweets': 1}
     ]
     },
    {'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': False,
     'tweet': [

     ]
     },
    {'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'whistle',
     'is_verified': True,
     'tweet': [

     ]
     },
]

no_of_user = len(users)
# print(len(users))
usernames = {user['user_name'] for user in users}
# print(usernames)

female_users = [user['name'] for user in users if user['gender'] == 'Female']
# print(female_users)

inactive_users = [user for user in users if len(user['tweet']) == 0]
# print(inactive_users)

name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
# print(name_and_age)

avg_age_of_user = round(sum(user['age'] for user in users) / len(users))
print(avg_age_of_user)
