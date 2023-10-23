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

    database_movies_prod = database_dir / 'movies_app.sqlite'
    """Archivo sqlite con los datos de las películas de producción
    """

    database_movies_test = database_dir / 'movies_app_test.sqlite'
    """Archivo sqlite con los datos de las películas de pruebas
    """
