import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

# loads method that can parse json string and return it as dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

#getting first langauge
print(dict_courses['languages'][0])

#********* Parse content present in Json file
with open('course.json') as f:
    data = json.load(f) 
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(type(data['dashboard']))
    print(data['dashboard']['website'])
    for course in data['courses']:
        if course['title'] == 'RPA':
            print(f"Price of {course['title']} course is {course['price']}")
            assert course['price'] == 50

with open('course1.json') as g:
    data2 = json.load(g)
    assert data == data2 # comparing data from 2 json files