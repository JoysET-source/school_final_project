from fastapi import FastAPI

# from src.routes.user_routes import router as router_users
# from src.routes.todo_routes import router as router_todo
# from src.database import Base, engine

# Create database tables
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(router_users)
# app.include_router(router_todo)


@app.get("/kitchen")
async def root():
    return {"message": "Welcome to Organizator de rețete culinare API"}

@app.get("/")
async def nome_ricetta(ricetta : str):
    return {"messaggio": f"stai cercando la ricetta {ricetta.capitalize()}"}

