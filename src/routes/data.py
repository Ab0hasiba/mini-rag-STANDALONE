from fastapi import FastAPI, APIRouter,Depends,UploadFile,File
import os
from helpers.config import get_settings,Settings

data_router=APIRouter(
    prefix='/api/version1/data',
    tags=['api_v1','data'],
)

@data_router.post("/upload?{project_id}")
async def upload(project_id:str,file:UploadFile,appsettings:Settings = Depends(get_settings)):
    
