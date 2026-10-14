from fastapi import FastAPI, APIRouter,Depends
import os
from helpers.config import get_settings,Settings

data_router=APIRouter(
    prefix='/api/version1/data',
    tags=['api_v1','data'],
)

@data_router.post("/upload?{}")
async def upload(appsettings:Settings = Depends(get_settings)):
    