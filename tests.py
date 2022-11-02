# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - present AppSeed.us
"""

import pytest
import json
import time
from api import app

import random
import string

"""
   Sample test data
"""

# TEST CASE #1: current dummy usersname should be able to do it
# TEST CASE #2: allows autogenerated usernames and emails and passwords to be created
DUMMY_USERNAME = "apple"
DUMMY_EMAIL = "apple@apple.com"
DUMMY_PASS = "newpassword"

def generateDummyData():
    # username with 5 characters:
    DUMMY_USERNAME_ = ''.join(random.choices(string.ascii_lowercase, k=5))
    DUMMY_EMAIL_ = DUMMY_USERNAME_ + "@apple.com"
     # password with 11 characters:
    DUMMY_PASS_ = ''.join(random.choices(string.ascii_lowercase, k=11))
    return DUMMY_USERNAME_, DUMMY_EMAIL_, DUMMY_PASS_




@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

    print("setting random here!")


def test_creating_learning_journey(client):
    from random import randint
    value = randint(0, 200)
    response = client.post(
        "api/users/register2",
        data=json.dumps(
            {
                "name": f"#{value} journey",
            }
        ),
        content_type="application/json")

    print("The user was successfully registered")
    data = json.loads(response.data.decode())
    print("RESULT:", data)
    assert response.status_code == 200
    assert "The Learning journey was successfully registered" in data["msg"]




def test_user_signup1(client):
    """
       Tests /users/register API
    """
    DUMMY_USERNAME_RANDOM, DUMMY_EMAIL_RANDOM, DUMMY_PASS_RANDOM = generateDummyData()
    print("generated: ",{
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            } )
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")

    print("The user was successfully registered")
    data = json.loads(response.data.decode())
    print("RESULT:", data)
    assert response.status_code == 200
    assert "The user was successfully registered" in data["msg"]
    
def test_user_signup_duplicate(client):
    """
       Tests '/users/register' API
    """
    DUMMY_USERNAME_RANDOM, DUMMY_EMAIL_RANDOM, DUMMY_PASS_RANDOM = generateDummyData()
    print("generated duplicate: ",{
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            } )
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")

    # time.sleep(10)
    responseDuplicate = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")

    # print("The user was successfully registered")
    data = json.loads(responseDuplicate.data.decode())
    print("RESULT:", data)
    assert responseDuplicate.status_code == 400
    assert "Email already taken" in data["msg"]
    


def test_user_signup_invalid_data(client):
    """
       Tests /users/register API: invalid data like email field empty
    """
    print("test_user_signup_invalid_data")
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME,
                "email": "",
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    # boundary testing and negative testing --- the toal length of email should be more than ....:
    assert "'' is too short" in data["msg"]


def test_user_login_correct(client):
    """
       Tests /users/signup API: Correct credentials
    """
    DUMMY_USERNAME_RANDOM, DUMMY_EMAIL_RANDOM, DUMMY_PASS_RANDOM = generateDummyData()
    # print("generated duplicate: ",{
    #             "username": DUMMY_USERNAME_RANDOM,
    #             "email": DUMMY_EMAIL_RANDOM,
    #             "password": DUMMY_PASS_RANDOM
    #         } )
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")
    print("test_user_login_correct")
    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["token"] != ""


def test_user_login_error(client):
    """
       Tests /users/signup API: Wrong credentials
    """
    print("test_user_login_error")

    DUMMY_USERNAME_RANDOM, DUMMY_EMAIL_RANDOM, DUMMY_PASS_RANDOM = generateDummyData()
    # print("generated duplicate: ",{
    #             "username": DUMMY_USERNAME_RANDOM,
    #             "email": DUMMY_EMAIL_RANDOM,
    #             "password": DUMMY_PASS_RANDOM
    #         } )
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_RANDOM,
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_PASS_RANDOM
            }
        ),
        content_type="application/json")


    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL_RANDOM,
                "password": DUMMY_EMAIL_RANDOM
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Wrong credentials." in data["msg"]