from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"Server is running": "1"}
