import json

def search_json(json_data, search_string):
    results = []
    
    for user in json_data:
        if search_string in user: 
            results.append(user[search_string])
            #print(user["User"], " contains ", user[search_string])


    return results