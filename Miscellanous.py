import requests

cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# timeout attribute to wait before taking response
# allow redirection = false is atribute that stops call after hitting redirection
# 30x - redirection code then it hits 200
# print(response.history) - checks history for redirections and etc
print(response.status_code)


# httpbin.org - cool website

ses = requests.session() # sesion manager is also pretty cool
ses.cookies.update({'visit-month':'February'})

res = ses.get('https://httpbin.org/cookies', cookies={'visit_yea':'January'})
print(res.text)

# attachments

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file':open('/Users/kacperbiegajlo/Downloads/Geri.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)