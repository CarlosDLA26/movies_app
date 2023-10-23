# External libraries
import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse

# Own libraries
from db import Base
from db import engine
from models.models import *
from python.metadata.tags import Tags
from python.paths import Paths
from routers.auth import auth_router
from routers.movies import movies_router


app = FastAPI()
app.title = 'API Películas'

app.include_router(movies_router)
app.include_router(auth_router)


@app.get('/', tags=[Tags.HOME.value])
def home():
    response = FileResponse(Paths.html_dir / 'home.html')
    return response


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, port=5000)