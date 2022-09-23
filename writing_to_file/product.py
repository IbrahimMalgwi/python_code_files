import pprint
from decimal import Decimal
import pickle
import json
import yaml

# products = [
#     {'name': 'Soap', 'Quantity': 3, 'Price': Decimal('23.50'), 'is_expired': False},
#     {'name': 'Tissue', 'Quantity': 6, 'Price': Decimal('20.00'), 'is_expired': False},
#     {'name': 'Durex', 'Quantity': 2, 'Price': Decimal('123.99'), 'is_expired': False},
#     {'name': 'Neck choke', 'Quantity': 1, 'Price': Decimal('239.99'), 'is_expired': True},
# ]

products = [
    {'name': 'Soap', 'Quantity': 3, 'Price': 23.50, 'is_expired': False},
    {'name': 'Tissue', 'Quantity': 6, 'Price': 20.00, 'is_expired': False},
    {'name': 'Durex', 'Quantity': 2, 'Price': 123.99, 'is_expired': False},
    {'name': 'Neck choke', 'Quantity': 1, 'Price': 239.99, 'is_expired': True},
]


with open('yaml_object.json', mode='w') as file:
    yaml.dump(products, file)

# with open('jason_object.json', mode='w') as file:
#     json.dump(products, file, indent=4)

# with open('jason_object.json', mode='r') as file:
#     x = json.load(file)
#     print(x)

# For pickle
# with open('pickled_object.txt', mode='wb') as file:
#     pickle.dump(products, file)
#
# with open('pickled_object.txt', mode='rb') as file:
#     x = pickle.load(file)
#     pprint.pprint(x, indent=4)
#
# print(0.1 + 0.2)
# print(Decimal(0.1) + Decimal(0.2) == 0.3)

# x = pickle.dumps(products)
# print(x)
