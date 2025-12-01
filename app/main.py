from fastapi import FastAPI
from services import get_video_metadata;
from schemas import *;

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome":"Bienvenido a la Api de Jhon Ruiz"}

@app.post("/metadata")
def metadata(data: YTVideo):
    url = str(data.url)
    info = get_video_metadata(url)
    return info