from fastapi import FastAPI
app = FastAPI()
@app.get("/")# / is a root
def home():
    return {"page": "Home"}
@app.get("/about")
def about():
    return {"page": "About","author":"Rakesh"}
@app.get("/health")
def health():
    return {"status": "ok"}
#Post request
@app.post("/create")
def create_something():
    return {"message": "created"}
#Path parameters with type Hint
@app.get("/candidate/{roolno}")
def get_candidate(roolno:int):
    return {"Result":"Distinction","roolno":roolno,"type":str(type(roolno))}

##HTTP methods
#Are a way to talk (from browser) to the server
#methods
#GET: Read data
#post: Create new data
#put:Replace existing data
#PAth
