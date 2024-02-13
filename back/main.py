
from fastapi import FastAPI
from database.engine import initialize_database
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import aliased
from routers import Users
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
initialize_database()



app.include_router(Users.router,  tags=["Users"])

