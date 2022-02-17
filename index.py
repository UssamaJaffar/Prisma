from fastapi import FastAPI
import uvicorn
from routes.Vehical_url import vehicle

app = FastAPI()
app.include_router(vehicle)

