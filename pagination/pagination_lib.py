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
Request information from the Meraki Dashboard API via pagination 
using the Meraki Dashboard API Python Library.
'''
def request_data_via_pagination():

    #Meraki Dashboard API Python Library offers: Get all (or a specified number of) pages of data with built-in pagination control  
    response = DASHBOARD.organizations.getOrganizationApiRequests(ORGA_ID, total_pages=TOTAL_PAGES, perPage=PER_PAGE) 
    
    helper.write_data_to_file('pagination_lib.json', response)
    print(f'-----{len(response)} new entries added stored in the pagination_lib.json . Meraki Dashboard API Python Library offers built-in pagination control.')


if __name__ == "__main__":
    load_dotenv()

    BASE_URL = os.environ['BASE_URL']
    ORGA_ID = os.environ['ORGA_ID']
    TOTAL_PAGES= "all" #integer that specifies the number of pages to retrieve. If you want the library to automatically retrieve all pages, then just pass in -1 or the string "all" for total_pages. Use with perPage to get total results up to total_pages*perPage.
    PER_PAGE = int(os.environ['PER_PAGE']) # optional integer value that specifies number of entries per page. Even without it the lib will use pagination.

    DASHBOARD = meraki.DashboardAPI(
        api_key = os.environ['API_TOKEN'],
        base_url= BASE_URL,
        output_log=False,
        print_console=True
        )

    request_data_via_pagination()