from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from schema.response_entity import ResponseMessage, ResponseEntity
from controller.user_controller import router

apps = FastAPI()

@apps.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
  response: ResponseMessage = ResponseMessage(
    code=exc.status_code,
    status="Error",
    message=exc.detail
  )
  return JSONResponse(status_code=exc.status_code, content=response.model_dump())

@apps.get("/", response_model=ResponseEntity[str])
async def root():
    return ResponseEntity(code=200, status="OK", message="Hello World from FastAPI")
  
apps.include_router(router)