from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def hello():
    return {"greeting": "Hello World!"}


client = TestClient(app)


def test_working():
    """make sure pytest works ok"""
    assert 1 == 1


def test_hello():  # intentionally not async
    """test hellow world home route function"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello World!"}


# command line: pytest fastapi_test.py
# see more advanced tests here: https://fastapi.tiangolo.com/tutorial/testing/?h=testing
