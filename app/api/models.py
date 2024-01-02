# app/api/models.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Table1(Base):
    __tablename__ = "table1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Add other columns as needed

class Table2(Base):
    __tablename__ = "table2"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    # Add other columns as needed
