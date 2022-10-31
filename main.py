# server api nhận dạng mail là spam hay ko 

from typing import Union
import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


# Load model RandomForestClassifier đã đc huấn luyện để phân lớp  mail
loaded_model = pickle.load(open('./RandomForestClassifier.sav', 'rb'))


# data là nội dung mail người dùng tập từ phía client 
class Data(BaseModel):
    data: str
   

# Gọi FastApi để viết file api
app = FastAPI()


# hàm đc gọi khi client truy cập đến trang chủ
@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

# nhận dữ liệu từ cilent
@app.post("/prediction/")
async def predict_item(item: Data):

    # Gọi  model đã load để dự đoán 
    result =int(loaded_model.predict([item.data]))
    
    return  result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)