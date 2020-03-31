#1.import json library which It is derived from a version of the externally maintained simplejson library.
import json
from difflib import get_close_matches
#open json file
data = json.load(open("data.json"))    

def translate(w):
  
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Did you mean {} instead Enter Y if yes,or N if no : ".format (get_close_matches(w,data.keys())[0]))

        if yn =="Y" or yn == "Y".lower():
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn == "N".lower():
            return "Word doesn't exist.Confirm it again"
        else:
            return "We did not understand you"
        
    else:
        return "The word does not exist"

word = input("Enter word: ")

output = translate(word)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)