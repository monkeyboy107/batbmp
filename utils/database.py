from typing import List, Optional
from sqlalchemy import create_engine, select, ForeignKey, String, Column, Text
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_utils import database_exists, create_database

class db:
  def __init__(self, engine):
    self.engine = engine
    if not database_exsists(engine.url):
      create_database(engine.url)
  
  def add_host(self, mac):
    host = Host(mac=mac)
    with Session(self.engine) as session:
      session.add(host)
      session.commit()
  
  def find_host(self, mac):
    with Session(self.engine) as session:
      stmt = select(base.host.where(host.mac.in_([mac])))
      for host in session.scalers(stmt):
        print(host)

class Base(DeclarativeBase):
    pass

class Host(Base):
    __tablename__ = "hosts"
    id: Mapped[int] = mapped_column(primary_key=True)
    mac: Mapped[str] = mapped_column(String(18))

def generate_engine(connection_uri='sqlite:///:memory:'):
  return create_engine(connection_uri, echo=True)
