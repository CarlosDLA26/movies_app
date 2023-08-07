# External libraries
from pathlib import Path


class Paths:
    root = Path(__file__).parents[1]
    """Ruta a directorio raíz del proyecto
    """

    html_dir = root / 'html'
    """Ruta a directorio HTML con modelos de respuesta
    """
