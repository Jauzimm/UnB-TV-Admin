from fastapi.middleware.cors import CORSMiddleware
from fastapi import  FastAPI


from controller import pautaController
# import sys


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prefix="/api", router=pautaController.pauta)

@app.get("/")
def read_root():
    return {"message": "UnB-TV!"}
