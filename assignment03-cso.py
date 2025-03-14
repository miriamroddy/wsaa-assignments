# importing the required libraries
# changed from requests to from urllib3 so I could bypass SSL verification manually


import urllib3
import json


# I use my work laptop so I had to use cert_reqs='CERT_NONE' to disable SSL verification - not typically a good practice, I know
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)


# URL for CSO dataset:
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# try block - was handy when getting errors
# https://www.w3schools.com/python/python_try_except.asp
try:
    # send GET request
    response = http.request('GET', url)


    # then check - was request successful? 200 means OK
    if response.status == 200:
       
        with open("cso.json", "w") as file:
            #  convert JSON object to string and writes to file
            json.dump(json.loads(response.data.decode('utf-8')), file)
        print("Success! Dataset saved to cso.json")
    else:
        print(f"Failed to retrieve CAO data. Code: {response.status}")
       
# again, we want to catch exceptions
except Exception as e:
    print(f"Uh-oh. An error occurred: {e}")
