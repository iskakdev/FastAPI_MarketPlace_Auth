from fastapi import FastAPI
from api import (profile_api, auth)
import uvicorn

marketplace_app = FastAPI(title='FastAPI MarketPlace Auth')
marketplace_app.include_router(profile_api.user_router)
marketplace_app.include_router(auth.auth_router)

if __name__ == '__main__':
    uvicorn.run(marketplace_app, host='127.0.0.1', port=8000)
