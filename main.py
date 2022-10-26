from typing import Union
import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


loaded_model = pickle.load(open('./RandomForestClassifier.sav', 'rb'))

class Data(BaseModel):
    data: str
   


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/prediction/")
async def predict_item(item: Data):

    result =int(loaded_model.predict([item.data]))
    
    return  result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)