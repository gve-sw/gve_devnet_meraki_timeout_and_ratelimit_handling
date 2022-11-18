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
import meraki

'''
Request information from the Meraki Dashboard API and 
handle a too many requests error using the requests module.
'''
def execute_call_and_handle_429_error(DASHBOARD):

    #Meraki Dashboard API Python Library offers: Automatic retries upon 429 rate limit errors, using the Retry-After field within response headers
    DASHBOARD.organizations.getOrganizations()
    print(f'Call Executed')
    
    #Provoke a "too many request" error: uncomment the following line to create a request loop and run this script in min 5 windows in parallel to increase the load 
    #execute_call_and_handle_429_error(DASHBOARD)


if __name__ == "__main__":
    load_dotenv()

    API_TOKEN = os.environ['API_TOKEN']
    BASE_URL = os.environ['BASE_URL']

    DASHBOARD = meraki.DashboardAPI(
        api_key = os.environ['API_TOKEN'],
        base_url= BASE_URL,
        output_log=False,
        print_console=False
    )

    execute_call_and_handle_429_error(DASHBOARD)
