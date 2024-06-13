from fastapi import FastAPI
from fastapi import Request

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.operations.routers import router_calculate

app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request,
                                 exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.get('/')
def index():
    return {"Hello": "friend"}


app.include_router(router_calculate)
