import requests

# Authenticate and get the bearer token
auth_url = 'https://login.salesforce.com/services/oauth2/token'
data = {
    'grant_type': 'password',
    'username': 'udabby@powerorg23.demo',
    'password': 'salesforce1',
    'client_id': '3MVG9X12xD2kqQmY5q_tRorE.ODzCcfNF9Xu0a20TUOl09W.9UhPxXiQXlFQuhhPdwqGpNDZe8kLbQnu8pfEz',
    'client_secret': 'BA5FDAC2D4DE197B4F68041BEA4D85236E8BE08C91047EACA228966B6F0E03D9'
}
response = requests.post(auth_url, data=data)

if response.status_code == 200:
    bearer_token = response.json().get('access_token')
    # Use the bearer token to update the custom field
    update_url = 'https://udabby-230307-341-demo.my.salesforce.com//services/data/v58.0/sobjects/Asset/02iDm000001Ar2UIAS'
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'UD_Test__c': true
    }
    update_response = requests.patch(update_url, headers=headers, json=payload)
    
    if update_response.status_code == 204:
        print('Custom field updated successfully.')
    else:
        print('Failed to update custom field.')
else:
    print('Authentication failed.')
