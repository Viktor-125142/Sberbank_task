from fastapi import FastAPI
from fastapi import Request


from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.operations.routers import router_calculate

app = FastAPI(title="Calculate deposit")


@app.exception_handler(RequestValidationError)
def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
def internal_server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "error": str(exc)},
    )


@app.get('/')
def index():
    return {"Hello": "friend"}


app.include_router(router_calculate)
