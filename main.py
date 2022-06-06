from typing import Union
from fastapi import FastAPI, File, UploadFile
from src import api
import shutil
from fastapi.responses import FileResponse
import os
from io import BytesIO


app = FastAPI()


@app.get('/')
def read_root():
    return {
        'status': '200',
        'message': 'Send a request with post method to our endpoint and get your .csv file',
        'endpoint': 'localhost:8000/xlsx-to-csv',
        'keys': 'file: SEND_YOUR_FILE_HERE'
    }


@app.post('/xlsx-to-csv/')
async def files(file: UploadFile):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        csv_path = api.main(buffer.name)

    os.remove(buffer.name)
    return FileResponse(csv_path, media_type="xlsx/csv", filename=csv_path)
