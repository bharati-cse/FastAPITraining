from fastapi import FastAPI
app = FastAPI()
@app.get("/")# / is a root
def read_root():
    return {"message": " Hello World","number": 44,"is_fun": True}


