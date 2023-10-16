# External libraries
from pathlib import Path


class Paths:
    root = Path(__file__).parents[1]
    """Directorio raíz del proyecto
    """

    html_dir = root / 'html'
    """Directorio con archivos HTML de respuesta
    """

    database_dir = root / 'db'
    """Directorio con las configuraciones a las bases de datos
    """

    database_movies = root / 'movies_app.sqlite'
    """Archivo sqlite con los datos de las películas
    """
