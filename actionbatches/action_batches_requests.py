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

import json
import os
from dotenv import load_dotenv
import time
import requests


'''
Changes the name and tag configuration of the first three ports of 
a specific switch via Action Batches and the Python requests module.
'''
def configure_ports_with_action_batches(BASE_URL, HEADERS, ORGA_ID, SWITCH_SERIAL, WAITING_TIME_SEC):

    actions = [
        {
        "resource": f"/devices/{SWITCH_SERIAL}/switch/ports/1",
        "operation": "update",
        "body": {
            "name":'This switch port was updated via action batches 1',
            "tags":['updated_by_action_batch']
            }
        },
        {
            "resource": f"/devices/{SWITCH_SERIAL}/switch/ports/2",
            "operation": "update",
            "body": {
                "name":'This switch port was updated via action batches 1',
                "tags":['updated_by_action_batch']
            }
        },
        {
            "resource": f"/devices/{SWITCH_SERIAL}/switch/ports/3",
            "operation": "update",
            "body": {
                "name":'This switch port was updated via action batches 1',
                "tags":['updated_by_action_batch']
            }
        }
    ]

    actionBatchId = create_action_batch(BASE_URL, HEADERS, ORGA_ID, actions)
    print(f'Action batch was created.')

    completed = False
    failed = False

    while not completed and not failed:
        time.sleep(WAITING_TIME_SEC)
        completed, failed = check_action_batch_status(BASE_URL, HEADERS, ORGA_ID, actionBatchId)

    print(f'Action batch finished. Status - Completed: {completed}, Failed: {failed}')


'''
Creates an action batch for a chosen organization and actions.
Returns the id of the created batch.
'''
def create_action_batch(BASE_URL, HEADERS, ORGA_ID, actions):
    
    url = f'{BASE_URL}/organizations/{ORGA_ID}/actionBatches'

    payload = {
        "confirmed": True,
        "synchronous": False,
        "actions": actions
    }
    
    create_response = requests.request('POST', url, headers=HEADERS, data = json.dumps(payload)).json()
    
    action_batch_id = create_response['id']

    return action_batch_id 


'''
Checks the status of an action batch by its ID.
Returns completed and failed status
'''
def check_action_batch_status(BASE_URL, HEADERS, ORGA_ID, actionBatchId):
    
    url = f'{BASE_URL}/organizations/{ORGA_ID}/actionBatches/{actionBatchId}'
    payload = None

    check_response = requests.request('GET', url, headers=HEADERS, data = payload).json()

    completed = check_response['status']['completed']
    failed = check_response['status']['failed']

    return completed, failed


if __name__ == "__main__":
    load_dotenv()

    BASE_URL = os.environ['BASE_URL']
    ORGA_ID = os.environ['ORGA_ID']
    SWITCH_SERIAL = os.environ['SWITCH_SERIAL']
    WAITING_TIME_SEC = 5
    
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": os.environ['API_TOKEN']
    }

    configure_ports_with_action_batches(BASE_URL, HEADERS, ORGA_ID, SWITCH_SERIAL, WAITING_TIME_SEC)