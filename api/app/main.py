import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session
from .db import engine, get_db
from . import models, schemas

app = FastAPI(title="Wishlist API", openapi_url="/api/openapi.json")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok"}
    except SQLAlchemyError as e:
        return {"status": "db_error", "detail": str(e)}

@app.post("/api/items", response_model=schemas.ItemRead)
def create_item(payload: schemas.ItemCreate, db: Session = Depends(get_db)):
    ## Temp code: get or create user with id=1 (hard coded)
    owner = db.get(models.User, 1)
    if not owner:
        owner = models.User(email="demo@example.com", display_name="Demo", password_hash="x")
        db.add(owner); db.flush()

    item = models.Item(owner_id=owner.id, **payload.model_dump())
    db.add(item); db.commit(); db.refresh(item)
    return item

@app.get("/api/users/{user_id}/items", response_model=list[schemas.ItemRead])
def list_items(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Item).filter(models.Item.owner_id == user_id).order_by(models.Item.rank).all()
