import requests

from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        headers = {'Content-Type': 'application/json'}
        deleteBook_response = requests.post(url2, json={"ID": context.book_id}, headers=headers, )

        assert deleteBook_response.status_code == 200
        res_json = deleteBook_response.json()

        print(res_json['msg'])
        assert res_json['msg'] == "book is successfully deleted"