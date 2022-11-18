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

import meraki
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helper

'''
Request data for a specific timespan or time points via the Meraki Dashboard API Python Library.
'''
def request_data_for_specific_time(DASHBOARD, ORGA_ID, T0_EPOCH, T1_EPOCH, TIMESPAN_SEC):

    timespan_response = DASHBOARD.organizations.getOrganizationApiRequestsOverview(ORGA_ID, timespan=TIMESPAN_SEC)
    helper.write_data_to_file('timespan_lib.json', timespan_response)
    print(f'Pre-filtering response based on timespan: {timespan_response}')

    t0_t1_response = DASHBOARD.organizations.getOrganizationApiRequestsOverview(ORGA_ID, t0=T0_EPOCH, t1=T1_EPOCH)
    helper.write_data_to_file('t0_t1_lib.json', t0_t1_response)
    print(f'Pre-filtering response based on t0 and t1: {t0_t1_response}')


if __name__ == "__main__":
    load_dotenv()

    BASE_URL = os.environ['BASE_URL']
    ORGA_ID = os.environ['ORGA_ID']
    DAYS = os.environ['DAYS'] # Max 31 days

    T1_EPOCH, T0_EPOCH, TIMESPAN_SEC = helper.days_to_timeformats(0, DAYS) 
    
    DASHBOARD = meraki.DashboardAPI(
        api_key = os.environ['API_TOKEN'],
        base_url= BASE_URL,
        output_log=False,
        print_console=True
        )

    request_data_for_specific_time(DASHBOARD, ORGA_ID, T0_EPOCH, T1_EPOCH, TIMESPAN_SEC)