from fastapi import FastAPI

app = FastAPI()

@app.get("/liveness")
def liveness_check():
    return "OK"
