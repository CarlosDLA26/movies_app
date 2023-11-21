# Eternal libraries
import time
import traceback

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:

        """Función por la cual pasan todas las solicitudes para el manejo de
        errores.

        Args:
            request: solicitud de cliente.
            call_next: endpoint al que se realiza la solicitud.

        Returns:
            Response: Respuesta obtenida a partir del endpoint `call_next` 
        """

        try:
            start_time = time.time()
            res = await call_next(request)
            final_time = time.time() - start_time
            return res
        except Exception as e:
            final_time = time.time() - start_time
            msg = traceback.format_exc()
            return JSONResponse(
                content={
                    'error_msg': msg,
                    'time_ex': str(final_time)
                },
                status_code=500)
