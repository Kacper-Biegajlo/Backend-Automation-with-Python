import requests
import configparser
import json
from payLoad import *
from utilities.configurations import *
from utilities.resources import *

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': 'application/json'}
query = 'select * from Books'
addBook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers, )
                            
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

book_id = response_json["ID"]
print(book_id)

# Delete book -
url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers = {'Content-Type': 'application/json'}
deleteBook_response = requests.post(url2, json={"ID": book_id}, headers=headers,)

assert deleteBook_response.status_code == 200
res_json = deleteBook_response.json()

print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"

# authentication
# does not work but done that with steam key in my project from Python Crash course book
# url = 'https://api.github/com/BlueCodeMaster3000' 
# requests.get(url,auth=('BlueCodeMaster300',getPassword()))
se = requests.session()
se.auth = auth = ('BlueCodeMaster3000', getPassword())
url3 = 'https://api.github.com/repositories'

response = se.get(url3)
print(response.status_code) 

# wont work since github api changed
# made it work because I am GigaChad and Kaczor's padawan
