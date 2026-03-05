'''
Adan Rojas Design Code Practice => 03/02
---------------------------------------------------------
You're building a backend service that tracks user API requests. 
Given a list of log entries, each containing a user_id and a timestamp (in seconds), 
write a function that returns all users who made more than k requests within any sliding window of t seconds.

API Permission Tree
---------------------------------------------------------
'''

# There is 4 keys in the tree hash-map, 
# each key has a hash map with 2 key-value pairs
# Highkey this one is kinda hard bro!



def api_permission_tree(tree, queries) -> list:

    return_list = []

    for query in queries:
        user = query["user"]
        permission = query["permission"]

        if permission in tree and user in tree[permission]["users"]:
            return_list.append(True)
        else:
            # TODO: Implement recursive check through parent nodes
            return_list.append(False)
        
    return return_list

def main():
    tree = {
        "root": 
        {
            "children": ["admin", "viewer"], 
            "users": ["u1"]
        },
        "admin": 
        {
            "children": ["superadmin"], 
            "users": ["u2", "u3"]
        },
        "viewer": 
        {
            "children": [], 
            "users": ["u4"]
        },
        "superadmin": 
        {
            "children": [], 
            "users": ["u5"]
        },
    }

    queries = [
        {"user": "u5", "permission": "admin"},    # True  — u5 is under superadmin → admin → root
        {"user": "u4", "permission": "admin"},    # False — u4 is under viewer, not admin
        {"user": "u2", "permission": "root"},     # True  — u2 is under admin → root
        {"user": "u1", "permission": "root"},     # True  — u1 is directly at root
    ]

    result = api_permission_tree(tree, queries)
    print(result)

if "__main__" == __name__:
    main()