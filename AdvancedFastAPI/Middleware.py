from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["https://example.com"],
                   allow_methods=["GET", "POST"])

# Rest we can add our routes here like we did in the previous example.

