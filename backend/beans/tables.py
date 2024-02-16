from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

# Make the DeclarativeMeta
Base = declarative_base()

#Sql table example, tasks
class Task(Base):
    __tablename__ = 'tasks'
    def __init__(self, dict):
        self.id_task = dict['id_task']
        self.name = dict['name']
        self.begin_date = dict['begin_date']
        self.end_date = dict['end_date']
        self.id_parent_task = dict['id_parent_task']
    id_task = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    begin_date = Column(DateTime(timezone=True),
                            _default=func.now())
    end_date = Column(DateTime(timezone=True),
                            _default=func.now())    
    id_parent_task = Column(Integer)