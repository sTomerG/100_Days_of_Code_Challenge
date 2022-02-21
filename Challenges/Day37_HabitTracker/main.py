import re
import requests
from datetime import date


USERNAME = "tomergabay"
TOKEN = "pixela_endpoint"
GRAPH_ID = "day37challenge"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

def create_account():
    user_params = dict(
        token="pixela_endpoint",
        username="tomergabay",
        agreeTermsOfService="yes",
        notMinor="yes"
    )
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    response.raise_for_status()
    print(response.text)


def create_graph():
    graph_params = dict(
        id=GRAPH_ID,
        name="Coded today",
        unit="commit",
        type="int",
        color="sora",
    )
    
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=HEADERS)
    response.raise_for_status()
    print(response.text)
    
def post_pixel():
    post_pixel_params = dict(
        date = date.today().strftime("%Y%m%d"),
        quantity = '1'
    )
    response = requests.post(url=POST_PIXEL_ENDPOINT, json=post_pixel_params, headers=HEADERS)
    response.raise_for_status()
    print(response.text)
    
post_pixel()