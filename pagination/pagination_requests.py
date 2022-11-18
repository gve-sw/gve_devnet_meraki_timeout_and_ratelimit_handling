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
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helper


'''
Request information from the Meraki Dashboard API via pagination 
using the Python requests module.
'''
def request_data_via_pagination(BASE_URL, HEADERS, ORGA_ID, PER_PAGE):
    
    complete_response_data = []
    
    initial_url = f'{BASE_URL}/organizations/{ORGA_ID}/apiRequests?perPage={str(PER_PAGE)}'
    payload = None
 
    #Initial request
    print(f'-----Initial request url: {initial_url}')
    response = requests.get(initial_url, headers=HEADERS, data=payload)
    add_new_entries_to_summarizing_list(complete_response_data, response.json())

    #Concurrent requests
    while 'next' in response.links :

        next_link = response.links['next']['url'] #up to 4 options possible: next, prev, first, last
        print(f'-----Next request for link: {next_link}')

        response = requests.get(next_link, headers=HEADERS, data=payload)
        add_new_entries_to_summarizing_list(complete_response_data, response.json())

    helper.write_data_to_file('pagination_requests.json', complete_response_data)

    print(f'-----{len(complete_response_data)} entries stored in the pagination_requests.json file.')


'''
Appends all entries of a response to an overall list of all entries received via pagination. 
'''
def add_new_entries_to_summarizing_list(summarizing_list, new_entries_list):
    
    for entry in new_entries_list:  
        summarizing_list.append(entry)
    
    print(f'{len(new_entries_list)} new entries added to the response list.')


if __name__ == "__main__":
    load_dotenv()

    API_TOKEN = os.environ['API_TOKEN']
    BASE_URL = os.environ['BASE_URL']
    ORGA_ID = os.environ['ORGA_ID']
    PER_PAGE = int(os.environ['PER_PAGE'])

    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_TOKEN
    }

    request_data_via_pagination(BASE_URL, HEADERS, ORGA_ID, PER_PAGE)
