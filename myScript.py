import requests
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Script for updating a custom field in Salesforce.')
parser.add_argument('-u', '--username', help='Salesforce username')
parser.add_argument('-p', '--password', help='Salesforce password')
parser.add_argument('-id', '--client_id', help='Salesforce client ID')
parser.add_argument('-secret', '--client_secret', help='Salesforce client secret')
args = parser.parse_args()

# Authenticate and get the bearer token
auth_url = 'https://login.salesforce.com/services/oauth2/token'
data = {
    'grant_type': 'password',
    'username': args.username,
    'password': args.password,
    'client_id': args.client_id,
    'client_secret': args.client_secret
}
response = requests.post(auth_url, data=data)

if response.status_code == 200:
    bearer_token = response.json().get('access_token')
    # Use the bearer token to update the custom field
    update_url = 'https://udabby-230307-341-demo.my.salesforce.com/services/data/v58.0/sobjects/Asset/02iDm000001Ar2UIAS'
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'UD_Test__c': True
    }
    update_response = requests.patch(update_url, headers=headers, json=payload)

    if update_response.status_code == 204:
        print('Custom field updated successfully.')
    else:
        print('Failed to update custom field.')
else:
    print('Authentication failed.')
