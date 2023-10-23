# External libraries
from functools import lru_cache
from typing import Literal

# Own libraries
from python.paths import Paths


class EnvSettings():
    SQLALCHEMY_DATABASE_URL: str
    """Ruta a la base de datos sqlite de películas"""


class ProdConfig(EnvSettings):
    SQLALCHEMY_DATABASE_URL = f'sqlite:///{str(Paths.database_movies_prod)}'


class TestConfig(EnvSettings):
    SQLALCHEMY_DATABASE_URL = f'sqlite:///{str(Paths.database_movies_test)}'


class DevConfig(EnvSettings):
    SQLALCHEMY_DATABASE_URL = f'sqlite:///{str(Paths.database_movies_test)}'


@lru_cache()
def get_settings(env: Literal['dev', 'test', 'prod']) -> EnvSettings:

    """Obtiene las variabels de configuración según la modo de despliegue.

    Args:
        env: modo de despliegue. Solo hay tres valores posibles:
            - dev: modo de desarrollo
            - test: modo de pruebas
            - prod: modo de producción

    Returns:
        EnvSettings: clase con las variables según el modo de despliegue.

    Raises:
        ValueError: si el parámetro env no corresponde a ninguno de los valores
            disponibles.
    """

    modes = ['dev', 'test', 'prod']
    if env not in modes:
        raise ValueError(f'El modo de despliegue debe ser alguno {modes}')

    settings = {
        'dev': DevConfig,
        'test': TestConfig,
        'prod': ProdConfig
    }

    return settings[env]
