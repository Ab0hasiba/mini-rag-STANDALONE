from fastapi import FastAPI, APIRouter,Depends
import os
from helpers.config import get_settings,Settings

ini_router=APIRouter(
    prefix='/api/version1',
    tags=['api_v1'],
)
@ini_router.get("/")
async def welcome(appsettings:Settings = Depends(get_settings)):

    appname=appsettings.APP_NAME
    appversion=appsettings.APP_VERSION
    return {
        'appname' : appname,
        'appversion' : appversion,
    }


