from fastapi import FastAPI
from routers import productos,users,basic_auth_users,jwt_auth_users,users_db
from fastapi.staticfiles import StaticFiles
app = FastAPI()


#Routers
app.include_router(productos.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static",StaticFiles(directory="static"), name="static")



@app.get("/")
async def root():
    return 'Loading'

@app.get("/url")
async def url():
    return {"url linkedin":"https://www.linkedin.com/in/alejandra-garcia-sanchez-2513a212a/"}

# Inicia el server: uvicorn main:app --reload

#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc

