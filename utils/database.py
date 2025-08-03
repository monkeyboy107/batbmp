from typing import List, Optional
from sqlalchemy import create_engine, select, ForeignKey, String, Column, Text
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, registry
from sqlalchemy_utils import database_exists, create_database

# class Base(DeclarativeBase):
#     pass

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Host(Base):
    __tablename__ = "hosts"
    mac: Mapped[str] = mapped_column(String(18), primary_key=True)

class db:
  def __init__(self, engine):
    self.engine = engine
    if not database_exists(engine.url):
      create_database(engine.url)
      mapper_registry.metadata.create_all(engine)
      Base.metadata.create_all(engine)
  
  def add_host(self, mac):
    host = Host(mac=mac)
    with Session(self.engine) as session:
      session.add(host)
      session.commit()
  
  def find_host(self, mac):
    session = Session(self.engine)
    stmt = select(Host).where(Host.mac == mac)
    host = session.scalars(stmt)
    return host

def generate_engine(connection_uri='sqlite:///:memory:'):
  return create_engine(connection_uri, echo=True)
