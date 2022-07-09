import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to Library')
def step_imp(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayload('Poop4', '812362')

@when('we execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )

@then('the Book is successfully added')
def step_impl(context):
    response_json = context.response.json()
    context.book_id = response_json['ID']
    print(response_json["Msg"])
    print(response_json["ID"])
    assert response_json["Msg"] == "successfully added"



@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayload(isbn, aisle)

@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('BlueCodeMaster3000', getPassword())

@when('I hit getRepository API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)

@then(u'status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
