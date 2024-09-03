import requests

r = requests.get("https://www.codewithharry.com")
a=r.text
print(a)