# Importing the required libraries
import requests
import json

# URL for CSO dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Try block - helps catch errors
# https://www.w3schools.com/python/python_try_except.asp
try:
    # Send GET request
    response = requests.get(url)
    
    # Check if request was successful (200 means OK)
    if response.status_code == 200: