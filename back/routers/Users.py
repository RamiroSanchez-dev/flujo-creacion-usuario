from fastapi import APIRouter, status, HTTPException,Depends,  Body
from database.engine import initialize_database, get_local_session
from database.models import Users
from fastapi import HTTPException
from sqlalchemy.orm import aliased
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt
router = APIRouter()

API_TOKEN = "5edxbab5-c03f-46f0-aca2-4d75044c674c"
SECRET_KEY = "clave_secreta_deli"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def create_session_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/accounts/")
def check_app_password(
    data: dict = Body(...),
    token: str = Depends(oauth2_scheme),
):

    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token no válido")

    db = get_local_session()

    email = data.get("email")
    fullName = data.get("fullName")
    age = data.get("age")
    userName = data.get("userName")
    contry = data.get("contry")

    try:
        user = db.query(Users).filter(Users.email == email).first()
        if user:
            raise HTTPException(status_code=400, detail="Existe un usuario creado con dicho mail")
        else:
            new_user = Users(email=email, fullName=fullName, age=age,userName =userName,contry=contry )
            db.add(new_user)
            db.commit()
            user = new_user

        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token_data = {"sub": user.email, "exp": expires_delta.total_seconds()}
        session_token = create_session_token(token_data, expires_delta)
        return {"message": "Usuario creado exitosamente", "session_token": session_token}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
