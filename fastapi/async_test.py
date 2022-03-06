# test time for async vs non-async fastapi routes
# same content
# test each twice in opposite order to avoid caching effects, if any
# must have server running to test

import requests
from datetime import datetime

start = datetime.now()
requests.get("http://0.0.0.0:8001/not-async")
print(f"not-async time: {datetime.now() - start}")

start = datetime.now()
requests.get("http://0.0.0.0:8001/yes-async")
print(f"yes-async time: {datetime.now() - start}")

start = datetime.now()
requests.get("http://0.0.0.0:8001/yes-async")
print(f"yes-async time: {datetime.now() - start}")

start = datetime.now()
requests.get("http://0.0.0.0:8001/not-async")
print(f"not-async time: {datetime.now() - start}")
