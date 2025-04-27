from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
  
user = {1, "Bapi", "bapi@email.com"}
  
   

@app.get("/")
def read_root():
    return {'user':{'id': 1,
                    'name':'bapi',
                    'email':'bapi@email.com'} }