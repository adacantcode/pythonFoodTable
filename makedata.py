# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
from pathlib import Path
import re


def split_camel_case(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)

idDictionary = {}
imageDictionary = {}
allDictionary = {}

foodDictionary={}
utilityDictionary={}

with open("ids/allfoodimages.txt", "r") as idfile:
    for line in idfile:
        line = line.strip()
        if "=" in line:  # Ensure the line contains '=' before splitting
            key, value = line.split("=", 1)  # Split at the first '=' to avoid issues
            #key = split_camel_case(key)
            foodDictionary[key.strip()] = value.strip()  # Trim spaces around keys/values

with open("ids/allutilityimages.txt", "r") as imagefile:
    for line in imagefile:
        line = line.strip()
        if "=" in line:  # Ensure the line contains '=' before splitting
            key, value = line.split("=", 1)  # Split at the first '=' to avoid issues
            #key = split_camel_case(key)
            utilityDictionary[key.strip()] = value.strip()  # Trim spaces around keys/values

#and now lets compare the two dicts and combine into one

#for key in idDictionary:
#    if key in imageDictionary:
#        #print(key+" "+idDictionary[key]+" "+imageDictionary[key])
#        allDictionary[idDictionary[key]] = (key,imageDictionary[key])
#    else:
#        pass

#print(allDictionary)

with open("foodimages.txt", "w") as jfile:
    json.dump(foodDictionary, jfile, indent=4)
with open("utilityimages.txt", "w") as jfile:
    json.dump(utilityDictionary, jfile, indent=4)