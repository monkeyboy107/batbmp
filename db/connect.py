from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Host(Base):
  __tablename__ = "host"
  id = Column(Integer, primary_key=True)
  host = Column(String)
  name = Column(String)

engine = create_engine("sqlite:///:memory")
