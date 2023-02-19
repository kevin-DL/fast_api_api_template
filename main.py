from fastapi import FastAPI, APIRouter

from api.routes import items, auth, users

app = FastAPI()

api_router = APIRouter()
api_router.include_router(auth.router)


api_router.include_router(users.router)
api_router.include_router(items.router)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
