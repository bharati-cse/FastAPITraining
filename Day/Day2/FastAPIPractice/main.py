from fastapi import FastAPI
from pydantic import BaseModel
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
@app.get("/student/{usn}")
def get_student(usn):
      return {"Result": "Distinction", "usn": usn}
#Path parameters with type Hint
@app.get("/candidate/{roolno}")
def get_candidate(roolno:int):
    return {"Result":"Distinction","roolno":roolno,"type":str(type(roolno))}
#pydantic model
class Item(BaseModel):
    name:str
    price:float
    is_stock:bool=True
@app.post("/items")
def create_item(item:Item):
    return {"received":item,"total_price":item.price*1.18}
##HTTP methods
#Are a way to talk (from browser) to the server
#methods
#GET: Read data
#post: Create new data
#put:Replace existing data
#
