# importing the required libraries
# changed from requests to from urllib3 so I could bypass SSL verification manually


import urllib3
import json


# I use my work laptop so I had to use cert_reqs='CERT_NONE' to disable SSL verification - not typically a good practice, I know
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)


# URL for CSO dataset:
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Try block - helps catch errors
# https://www.w3schools.com/python/python_try_except.asp
try:
    # Send GET request
    response = requests.get(url)
    
    # Check if request was successful (200 means OK)
    if response.status_code == 200:
                with open("cso.json", "w") as file:
            # Convert JSON response to a Python object and write to file
            json.dump(response.json(), file)
            
        print("Success! Dataset saved to cso.json")
    else:
        print(f"Failed to retrieve CSO data. Code: {response.status_code}")

# Again, we want to catch exceptions
except requests.exceptions.RequestException as e:
    print(f"Uh-oh. An error occurred: {e}")