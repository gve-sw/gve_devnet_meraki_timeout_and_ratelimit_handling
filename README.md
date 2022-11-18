# gve_devnet_meraki_timeout_and_ratelimit_handling

This repository contains multiple basic sample scripts that show techniques for rate limit and timeout handling in combination with the Meraki Dashboard API.

Example script overview:
1. **Too many Requests:** Script executes the [Get Organizations](https://developer.cisco.com/meraki/api-latest/#!get-organizations) endpoint and handles an automatic retry when a 429 (Too many Requests) error occurs. To provoke an "Too many Requests" error: uncomment the highlighted commands in the script to create a request loop and run the script in at least 5 command line windows in parallel.
2. **Pagination:** Script executes the [Get Organization Api Requests](https://developer.cisco.com/meraki/api-latest/#!get-organization-api-requests) endpoint with pagination.
3. **Pre-Filtering Parameters:** Script executes the [Get Organization Api Requests Overview](https://developer.cisco.com/meraki/api-latest/#!get-organization-api-requests-overview) endpoint and filters based on the timespan, t0 and t1 parameter.
4. **Action Batches:** Script executes the [Update Device Switch Port](https://developer.cisco.com/meraki/api-latest/#!update-device-switch-port) endpoint to change the name and tag of the first three ports of a switch based on action batches. 

Each of the mentioned scripts is available as a version using the Python requests module and a version using the Meraki Dashboard API Python Library.

## Contacts
* Ramona Renner


## Solution Components
Meraki Dashboard with:
* Min 1 Organization
* Meraki MS 

## Installation

1. Make sure you have [Python 3.8.0](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

2. Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html)).

3. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```

4. Clone this Github repository:  
  ```git clone [add github link here]```
  * For Github link: 
      In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
      ![/IMAGES/giturl.png](/IMAGES/giturl.png)
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it

5. Access the downloaded folder:  
    ```cd gve_devnet_meraki_timeout_and_ratelimit_handling```

6. Install all dependencies:  
  ```pip install -r requirements.txt```

7. Follow the instructions under https://developer.cisco.com/meraki/api/#!authorization/obtaining-your-meraki-api-key to obtain the **Meraki API Token**. Save the token for a later step.

8. Fill in your variables in the **.env** file:      
      
  ``` 
    API_TOKEN="[Add Meraki API key (see step 7)]"
    BASE_URL="https://api.meraki.com/api/v1/"
    
    ORGA_ID="[Add ID of Organization to apply chances to]"

    PER_PAGE="[Add number of entries per request/page (related to script "Pagination")]"
    
    DAYS="[Add number of days to request data for - max 31 days (related to script: "Pre-Filtering Parameters")]"

    SWITCH_SERIAL="[Add switch serial number of a device to change tag and name settings for (related to script: "Action Batches")]" 
  ```

  > Note: Mac OS hides the .env file in the finder by default. View the demo folder for example with your preferred IDE to make the file visible. 

  > Note: An easy way to find out the ID of an organization is to use the interactive documentation under: https://developer.cisco.com/meraki/api-v1/#!get-organizations 


## Usage

9. Access the folder of the preferred script   
    ```cd [add name of preferred script folder]```


10. Run the preferred script    
  ```python3 [add name of preferred script].py```


## More Useful Resources
* Meraki Dashboard API Python Library: https://pypi.org/project/meraki/, https://github.com/meraki/dashboard-api-python/
* Meraki Rate Limit Handling: https://developer.cisco.com/meraki/api-v1/#!rate-limit 
* Meraki Pagination: https://developer.cisco.com/meraki/api-latest/#!pagination/pagination
* Meraki Action Batches: https://developer.cisco.com/meraki/api-v1/#!overview/action-batches


# Screenshots
The first image of each section is the script using the Python requests module. The second script of each section is using the Meraki Dashboard API Python Library.
Scripts, using the Meraki Dashboard API Python Library use in most cases the optional "print_console" logging. 

### Too many Requests: 
![/IMAGES/0image.png](/IMAGES/screenshot_automatic_retry_requests.png)
![/IMAGES/0image.png](/IMAGES/screenshot_automatic_retry_lib.png)

### Pagination:
![/IMAGES/0image.png](/IMAGES/screenshot_pagination_requests.png)
![/IMAGES/0image.png](/IMAGES/screenshot_pagination_lib.png)

### Pre-Filtering Parameters: 
![/IMAGES/0image.png](/IMAGES/screenshot_timespan_requests.png)
![/IMAGES/0image.png](/IMAGES/screenshot_timespan_lib.png)

### Action Batches: 
![/IMAGES/0image.png](/IMAGES/screenshot_action_batches_requests.png)
![/IMAGES/0image.png](/IMAGES/screenshot_action_batches_lib.png)


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
