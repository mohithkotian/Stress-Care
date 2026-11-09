from fastapi import APIRouter, HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token
from passlib.context import CryptContext
from pydantic import BaseModel
from config.database import db
from utils.jwt_handler import create_token
import os
import re

router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


class SignUpRequest(BaseModel):
    full_name: str
    email: str
    password: str


class SignInRequest(BaseModel):
    email: str
    password: str


class GoogleAuthRequest(BaseModel):
    id_token_str: str


def is_valid_password(password: str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#]).{8,}$'
    return re.match(pattern, password)


@router.post("/signup")
def signup(data: SignUpRequest):
    users = db["users"]

    if users.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    if not is_valid_password(data.password):
        raise HTTPException(
            status_code=400,
            detail="Weak password. Must be 8+ characters with uppercase, lowercase, number, and special character.",
        )

    hashed_password = pwd_context.hash(data.password[:72])
    result = users.insert_one({
        "full_name": data.full_name,
        "email": data.email,
        "password": hashed_password,
    })

    token = create_token({
        "user_id": str(result.inserted_id),
        "email": data.email,
        "full_name": data.full_name,
    })

    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id),
        "token": token,
    }


@router.post("/signin")
def signin(data: SignInRequest):
    users = db["users"]
    user = users.find_one({"email": data.email})

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not pwd_context.verify(data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_token({
        "user_id": str(user["_id"]),
        "email": user["email"],
        "full_name": user["full_name"],
    })

    return {"message": "Login successful", "token": token}


@router.post("/google")
def google_auth(data: GoogleAuthRequest):
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=503, detail="Google authentication is not configured")

    try:
        claims = id_token.verify_oauth2_token(
            data.id_token_str,
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    email = claims.get("email")
    full_name = claims.get("name") or claims.get("given_name") or "Google User"
    if not email or claims.get("email_verified") is not True:
        raise HTTPException(status_code=401, detail="Google account email is not verified")

    users = db["users"]
    user = users.find_one({"email": email})

    if not user:
        result = users.insert_one({
            "full_name": full_name,
            "email": email,
            "is_google_auth": True,
        })
        user_id = str(result.inserted_id)
    else:
        user_id = str(user["_id"])

    token = create_token({
        "user_id": user_id,
        "email": email,
        "full_name": full_name,
    })

    return {"message": "Google Login successful", "token": token}
