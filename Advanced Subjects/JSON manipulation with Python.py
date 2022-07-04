from dataclasses import dataclass
import json
data='''{
    "name" : "Dude",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"]) # access value of key "email" within dict within dict within python file

