derrick = {'name': 'Derrick', 'age': 18, 'status': 'married', 'gender': 'F',}

for key in derrick.values():
    print(key)

for key in derrick.items():
    print(key)

for key, value in derrick.items():
    print(f"{key}--> {value}")