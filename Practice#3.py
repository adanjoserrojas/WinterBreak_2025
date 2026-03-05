'''
Adan Rojas Design Code Practice => 03/02
---------------------------------------------------------
You're building a backend service that tracks user API requests. 
Given a list of log entries, each containing a user_id and a timestamp (in seconds), 
write a function that returns all users who made more than k requests within any sliding window of t seconds.

API Rate Limit Tracker
---------------------------------------------------------
'''

logs = [
    {"user_id": "u1", "timestamp": 3},
    {"user_id": "u1", "timestamp": 2},
    {"user_id": "u1", "timestamp": 4},
    {"user_id": "u2", "timestamp": 1},
    {"user_id": "u2", "timestamp": 100},
    {"user_id": "u1", "timestamp": 7},
]
k = 3  # max allowed requests
t = 5  # sliding window in seconds

def api_rate_limiter():
    
    user_id_frequency = {}
    flagged_users = []
    # Use a sliding window of length = 2, subtract the start and end, and keep a counter of request/ second

    for i in range(len(logs)):
        
        if logs[i]["user_id"] not in user_id_frequency:
            user_id_frequency[logs[i]["user_id"]] = []

        user_id_frequency[logs[i]["user_id"]].append(logs[i]["timestamp"])
    
    for user in user_id_frequency:
        user_id_frequency[user] = sorted(user_id_frequency[user])

    for user, timestamps in user_id_frequency.items():
        left = 0
        for right in range(len(timestamps)):
            while timestamps[right] - timestamps[left] > t:
                left += 1
            
            if(right - left + 1) > k:
                flagged_users.append(user)
                break

    return flagged_users

# Time complexity is O(2n + n*m) = > O (n*m)!!!

def main():

    result = api_rate_limiter()
    print(result)

if "__main__" == __name__:
    main()