# External libraries
from fastapi import FastAPI
from fastapi.responses import FileResponse

# Own libraries
from metadata.tags import Tags
from metadata.paths import Paths
from routers.movies import movies_router


app = FastAPI()
app.title = 'API Películas'

app.include_router(movies_router)


@app.get('/', tags=[Tags.HOME.value])
def home():
    response = FileResponse(Paths.html_dir / 'home.html')
    return response


if __name__ == '__main__':
    print(Paths.root)