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

import os
from dotenv import load_dotenv
import requests
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helper

'''
Request data for a specific time  or time points via the Meraki Dashboard API and Python requests module.
'''
def request_data_for_specific_time(BASE_URL, HEADERS, ORGA_ID, T0_EPOCH, T1_EPOCH, TIMESPAN_SEC):

    ENDPOINT = f'/organizations/{ORGA_ID}/apiRequests/overview'
    payload = None

    url = BASE_URL + ENDPOINT + "?timespan=" + str(TIMESPAN_SEC)
    timespan_response = requests.get(url, headers=HEADERS, data=payload).json()
    print(f'Response based on timespan: {timespan_response}')
    helper.write_data_to_file('timespan_requests.json', timespan_response)

    url = BASE_URL + ENDPOINT + "?t0=" + str(T0_EPOCH) + "&t1=" + str(T1_EPOCH)  
    t0_t1_response = requests.get(url, headers=HEADERS, data=payload).json()
    print(f'Response based on time points: {t0_t1_response}')
    helper.write_data_to_file('t0_t1_requests.json', timespan_response)


if __name__ == "__main__":
    load_dotenv()

    BASE_URL = os.environ['BASE_URL']
    ORGA_ID = os.environ['ORGA_ID']
    API_TOKEN = os.environ['API_TOKEN']
    DAYS = os.environ['DAYS'] # Max 31 days

    T1_EPOCH, T0_EPOCH, TIMESPAN_SEC = helper.days_to_timeformats(0, DAYS) 
    
    HEADERS = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": API_TOKEN
        }

    request_data_for_specific_time(BASE_URL, HEADERS, ORGA_ID, T0_EPOCH, T1_EPOCH, TIMESPAN_SEC)