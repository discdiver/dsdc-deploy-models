from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/predict/")
async def make_prediction(
