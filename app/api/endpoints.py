# app/api/endpoints.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import crud
from app.api.database import SessionLocal, database
from app.api.models import Table1, Table2

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{table_name}/all", response_model=list[Table1])
def read_all_data(table_name: str, db: Session = Depends(get_db)):
    return crud.get_all_data(table_name, db)

@router.get("/{table_name}/row/{row_id}", response_model=Table1)
def read_row_data(table_name: str, row_id: int, db: Session = Depends(get_db)):
    return crud.get_row_data(table_name, row_id, db)

@router.get("/{table_name}/columns", response_model=list[str])
def read_column_names(table_name: str, db: Session = Depends(get_db)):
    return crud.get_column_names(table_name, db)

@router.get("/{table_name}/multiple/{column_name}", response_model=list)
def read_multiple_data(table_name: str, column_name: str, db: Session = Depends(get_db)):
    return crud.get_multiple_data(table_name, column_name, db)
