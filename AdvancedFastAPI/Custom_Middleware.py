from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app=FastAPI()

class SimpleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Before request")
        response = await call_next(request)
        print("After request")
        return response

app.add_middleware(SimpleMiddleware)

#Add a router
@app.get("/")
async def read_root():
    return {"message": "Hello World"}