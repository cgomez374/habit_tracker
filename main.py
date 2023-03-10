import requests
from datetime import datetime

TOKEN = 'INSERT TOKEN HERE'
USERNAME = 'INSERT USERNAME HERE'
GRAPH_ID = 'graph1'
TODAY = str(datetime.today().date()).replace('-', '')

# Create a user in Pixela

pixela_endpoint = 'https://pixe.la/v1/users'
params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=params)

# Create a graph via POST request

create_graph_endpoint = pixela_endpoint + f'/{USERNAME}/graphs'
headers = {
    'X-USER-TOKEN': TOKEN
}
body = {
    'id': GRAPH_ID,
    'name': 'cycling tracker',
    'unit': 'km',
    'type': 'int',
    'color': 'momiji'
}
# response = requests.post(url=create_graph_endpoint, headers=headers, json=body)

# Post values to the graph

post_values_endpoint = create_graph_endpoint + f'/{GRAPH_ID}'

data_to_post = {
    'date': TODAY,
    'quantity': '9'
}

# response = requests.post(url=post_values_endpoint, headers=headers, json=data_to_post)

# Put or update data

update_endpoint = post_values_endpoint + f'/{TODAY}'
data_to_update = {
    'quantity': '9'
}
response_status_code = 0
while response_status_code != 200:
    print('Trying..')
    response = requests.put(url=update_endpoint, headers=headers, json=data_to_update)
    response_status_code = response.status_code

print('Success!')






