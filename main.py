from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()


origins = [
    #"http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
user = {1, "Bapi", "bapi@email.com"}
  
   

@app.get("/users")
def read_root():
    return  [{'id': 1,
                    'name':'bapi',
                    'email':'bapi@email.com' }
             ]
    # return  {   'name':'bapi'  }
             