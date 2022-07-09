from utilities.configurations import *

def addBookPayload(isbn,aisle):
    body = {
 
        "name":"Teaching Automation Snake",
        "isbn": isbn,
        "aisle": aisle,
        "author":"Kacper"
    }
    print(body)
    return body

  

def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody