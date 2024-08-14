import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = ####
TOKEN = ####token
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)
now = dt.datetime.now()

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

quantity = "10"

pixel_config ={
    "date": now.strftime("%Y%m%d"),
    "quantity": quantity
}

# response = requests.post(url= pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


now = dt.datetime.now()

pixel_edit_endpoint = f"{pixel_endpoint}/{now.strftime('%Y%m%d')}"

quantity = "10"

pixel_edit_config ={
    "quantity": quantity
}

response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_config, headers=headers)
print(response.text)

