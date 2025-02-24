from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from datetime import datetime

Base = declarative_base()


class Task(Base):
    __tablename__ = 'TASK'  # Table name in DB

    # Maps attribute 'id' to DB column 'ID'
    id = Column('ID', Integer, primary_key=True)
    description = Column('TASK_DESCRIPTION', String)
    is_completed = Column('IS_COMPLETED', Boolean, default=False)
    inderted_at = Column('INSERTED_AT', DateTime, default=func.now())
    updated_at = Column('UPDATED_AT', DateTime)

    def to_dict(self):
        """ Properly serialize all fields to a dictionary """
        result = {}
        for c in inspect(self).mapper.column_attrs:
            value = getattr(self, c.key)
            if isinstance(value, datetime):
                result[c.key] = value.isoformat()  # Handle datetime fields
            else:
                result[c.key] = value
        return result


# SQLite connection
engine = create_engine('sqlite:///task_management.db')

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Session factory
SessionLocal = sessionmaker(bind=engine)
