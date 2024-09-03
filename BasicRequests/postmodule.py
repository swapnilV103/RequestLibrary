import requests
data={"id": "10",
        "courses": [
            "Python",
            "Java"
        ],
        "phone": "9047463323",
        "name": "swapnil",
        "location": "baramati"}

resp = requests.post("http://localhost:3000/people", json = data)
print(resp.status_code)
#print(resp.headers["content-type"])
print(resp.text)