'''
Adan Rojas Design Code Practice => 03/02
---------------------------------------------------------
Cache api usage and group in Hash Map by joining user-body
---------------------------------------------------------
'''





responses = [
    {"url": "/api/users/1",   "status_code": 200, "body": "{'name': 'Alice'}"},
    {"url": "/api/users/2",   "status_code": 200, "body": "{'name': 'Bob'}"},
    {"url": "/api/users/3",   "status_code": 200, "body": "{'name': 'Alice'}"},
    {"url": "/api/users/4",   "status_code": 200, "body": "{'name': 'Alice'}"},
    {"url": "/api/health",    "status_code": 200, "body": "{'name': 'Bob'}"},
    {"url": "/api/health",    "status_code": 200, "body": "{'name': 'Eve'}"},
    {"url": "/api/2",    "status_code": 200, "body": "{'name': 'Eve'}"},
]

target_key = "body"

def cache_group_body():

    r_dictionary = {}
    list_of_keys = []
    for i in range(len(responses)):
        if (responses[i][target_key] not in r_dictionary):
            r_dictionary[responses[i][target_key]] = []
            list_of_keys.append(responses[i][target_key])
        
        r_dictionary[responses[i][target_key]].append(responses[i]["url"])

    for i in range(len(r_dictionary)):
        if len(r_dictionary[list_of_keys[i]]) <= 1:
            del r_dictionary[list_of_keys[i]]
    
    return r_dictionary

def main():
    cache = cache_group_body()
    print(cache)

if "__main__" == __name__:
    main()