# app/api/crud.py
from sqlalchemy.orm import Session
from app.api.models import Table1, Table2

def get_all_data(table_name: str, db: Session):
    model = globals()[table_name]
    return db.query(model).all()

def get_row_data(table_name: str, row_id: int, db: Session):
    model = globals()[table_name]
    return db.query(model).filter(model.id == row_id).first()

def get_column_names(table_name: str, db: Session):
    model = globals()[table_name]
    return model.__table__.columns.keys()

def get_multiple_data(table_name: str, column_name: str, db: Session):
    model = globals()[table_name]
    return db.query(getattr(model, column_name)).all()
