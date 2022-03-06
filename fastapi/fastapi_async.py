# testing async vs sync function times
# no difference so far

import uvicorn
from fastapi import FastAPI
from datetime import datetime
import pandas as pd
import time


app = FastAPI()

# urls = [
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv",
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv",
# ]


# async def do_stuff_async():
#     """
#     tasks for to be done for testing how
#     """
#     vals = dict(zip(range(10_000_000), range(10_000_000)))
#     for url in urls:
#         pd.read_csv(url)
#     return


# def do_stuff_not_async():
#     """
#     tasks for to be done for testing how
#     """
#     vals = dict(zip(range(10_000_000), range(10_000_000)))
#     for url in urls:
#         pd.read_csv(url)
#     return


async def wait_seconds(seconds):
    time.sleep(seconds)


async def addition(a, b):
    await wait_seconds(3)
    print("Addition Result       : ", a + b)


async def multiplication(a, b):
    await wait_seconds(1)
    print("Multiplication Result : ", a * b)


async def division(a, b):
    await wait_seconds(5)
    print("Division Result       : ", a / b)


async def subtraction(a, b):
    await wait_seconds(7)
    print("Subtraction Result    : ", a - b)


@app.get("/yes-async")
async def demo2():

    await division(10, 20)
    await subtraction(10, 20)
    await addition(10, 20)
    await multiplication(10, 20)

    return "all clear from yes-async"


# not async
def nwait_seconds(seconds):
    time.sleep(seconds)


def naddition(a, b):
    nwait_seconds(3)
    print("Addition Result       : ", a + b)


def nmultiplication(a, b):
    nwait_seconds(1)
    print("Multiplication Result : ", a * b)


def ndivision(a, b):
    nwait_seconds(5)
    print("Division Result       : ", a / b)


def nsubtraction(a, b):
    nwait_seconds(7)
    print("Subtraction Result    : ", a - b)


@app.get("/not-async")
def demo1():
    ndivision(10, 20)
    nsubtraction(10, 20)
    naddition(10, 20)
    nmultiplication(10, 20)


if __name__ == "__main__":
    uvicorn.run("fastapi_async:app", reload=True, host="0.0.0.0", port=8001)
