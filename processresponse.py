import json
def processresponse(response):
    if response.status_code==200:
        return json.loads(response.content)
    elif response.status_code==403:
        print("Permission denied")
    elif response.status_code==404:
        print("Resource not found")