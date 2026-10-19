from fastapi import FastAPI, APIRouter,Depends,UploadFile,File,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings,Settings
from controllers.DataController import DataController
data_router=APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data'],
)

@data_router.post("/upload/{project_id}")
async def upload(project_id:str,file:UploadFile,appsettings:Settings = Depends(get_settings)):
    is_valid,Result_signal=DataController().validate_upload_file(file=file)
    if not is_valid:
        status_code=JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"signal":Result_signal})
  