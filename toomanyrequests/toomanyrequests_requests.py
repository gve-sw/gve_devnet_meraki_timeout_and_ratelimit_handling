""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

import requests
import os
import time
from dotenv import load_dotenv

'''
Request information from the Meraki Dashboard API and 
handle "too many requests" errors using the Python requests module.
'''
def execute_call_and_handle_429_error(BASE_URL, HEADERS):
        
    url = f'{BASE_URL}/organizations'
    payload = None

    response = requests.get(url, headers=HEADERS, data=payload)
    print(f'-----Call executed with status code: {response.status_code}')
    
    #Provoke a "too many request" error: uncomment the following 2 lines to create a request loop and run this script in min 5 windows in parallel to increase the load 
    #if response.status_code == 200:
    #    execute_call_and_handle_429_error(BASE_URL, HEADERS)

    if response.status_code == 429:
        print(f'''-----Error 429 (Too Many Requests). Retry in {response.headers["Retry-After"]} seconds -----''')
        time.sleep(int(response.headers["Retry-After"]))
        execute_call_and_handle_429_error(BASE_URL, HEADERS)


if __name__ == "__main__":
    load_dotenv()

    API_TOKEN = os.environ['API_TOKEN']
    BASE_URL = os.environ['BASE_URL']

    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_TOKEN
    }

    execute_call_and_handle_429_error(BASE_URL, HEADERS)
