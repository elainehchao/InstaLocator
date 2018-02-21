import requests

def getInstagramRequest():
    return requests.get('https://instagram.com')

print('Going to request from instagram')
request = getInstagramRequest()

# request response code
print("Request code: " + str(request.status_code))

# page source 
print("Requst text: " + str(request.text))
