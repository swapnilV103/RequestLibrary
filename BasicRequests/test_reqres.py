import requests
import pytest


def test_getre():
    head = {
        'Content-Type':'application/json'
    }

    resp = requests.get("https://reqres.in/api/users/2", headers=head)
    assert resp.status_code==200
    print(resp.status_code)
    print(resp.text)