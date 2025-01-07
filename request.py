import requests
import configuration
import data
from configuration import username, password
from data import auth_body, create_body


def create_token():
    return requests.post(configuration.URL_SERVICE + configuration.TOKEN, json=auth_body)

response = create_token()
print(response.status_code)
print(response.json()['token'])

def get_booking_ids():
    return requests.get(configuration.URL_SERVICE + configuration.GET_BOOKING_IDS)

response = get_booking_ids()
print(response.json())

def get_booking():
    return requests.get(configuration.URL_SERVICE + configuration.GET_BOOKING + configuration.ID)

response = get_booking()
print(response.json())

def post_create_booking():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_BOOKING, json=data.create_body)

response = post_create_booking()
print(response.status_code)
print(response.json())

id_path = str(response.json()['bookingid'])
print(id_path)

def get_booking_new():
    return requests.get(configuration.URL_SERVICE + configuration.GET_BOOKING + id_path)

response = get_booking_new()
print(response.json())

def put_bokking():
    return requests.put(configuration.URL_SERVICE + configuration.UPDATE_BOOKING + id_path, auth=(username,password), json=data.put_body)

response = put_bokking()
print(response.status_code)
print(response.json())



