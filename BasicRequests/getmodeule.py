import requests

r = requests.get("http://localhost:3000/people?id=5")
a=r.json()
assert r.status_code==200
print(r.status_code)
print(r.text)
print(a)
print(a[0]["courses"][0])
print(a[0]["id"])