'''
Adan Rojas Design Code Practice => 03/01
---------------------------------------------------------
Store endpoints that were used more than once by unique users 
---------------------------------------------------------
'''

input = ["u12:/api/orders",
         "u2:/api/profile",
         "u3:/api/education",
         "u4:/api/profile",
         "u1:/api/main",
         "u1:/api/main"]

end_marker = ":"

def userIdRequest(input, m) -> int:

    endpoints = {}
    returnStrings = []

    for i in range(len(input)):

        string = input[i]
        userId, path = string.split(":", 1)
        endpoints[path] = endpoints.get(path, set())
        endpoints[path].add(userId)

        if len(endpoints[path]) >= m and path not in returnStrings: returnStrings.append(path)

    return returnStrings

def main():
    strings = userIdRequest(input, 2)
    print(strings)

if "__main__" == __name__:
    main()