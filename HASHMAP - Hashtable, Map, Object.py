 #Dictionary - HASHMAP - Hashtable, Map, Object


#A dictionary is an unordered (key -> value) pair, you call the key, and get the value
dictionary = {
"mars": [1, 2, 3],
"venus": "love",
"jupiter" : True,
}

#lists are ordered with indexes
my_list = [
{
    "mars": [1, 2, 3],
    "venus": "love",
    "jupiter" : True,
},
{
    "mars": [4, 5, 6],
    "venus": "Petite Lune",
    "jupiter" : True,
}
]


print(dictionary["mars"][1]) #PRINTS FROM A DICTIONARY LOOKS FOR KEY "mars", THEN SHOWS INDICATED INDEX
print(my_list[0]["mars"][2]) #PRINTS FROM A LIST OF DICTIONARIES


print('love' in dictionary.values()) #RETURNS TRUE OR FALSE, .keys .values .items .clear .copy .pop .popitem

print (dictionary.update({"mars" : 55}))

print(dictionary)

