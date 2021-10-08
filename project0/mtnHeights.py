mountains = {
    "Mt. Everest" : "8,848",
    "K2" : "8,611",
    "Makalu" : "8,485"
}

for key in mountains.keys() :
    print(key)

for value in mountains.values() :
    print(value)

for key_name, value_name in mountains.items():
    print(key_name + " is " + value_name + "meters tall")