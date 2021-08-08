import json

numbers = [2, 4, 5, 6, 7]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
        
