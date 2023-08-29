import requests
# This method will make a request to the url and save the response to a file
def make_request_and_save_to_file(url, headers, filename):
    response = requests.get(url, headers=headers)
    
    with open(filename, 'w') as f:
        f.write(response.text)
        #returning the status code of the response
    return response
