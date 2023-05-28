"""Dict"""


dct1 = {}

dct2 = dict()

dct3 = {1: 1, 2: 2, 3: 3}

dct4 = {x: x for x in range (10)}

persons = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


for person in persons:
    print(person.get('age', 'Not in dict'))