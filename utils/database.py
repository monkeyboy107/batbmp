from typing import List, Optional
from sqlalchemy import create_engine, select, ForeignKey, String, Column, Text
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, registry
from sqlalchemy_utils import database_exists, create_database


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
    exists = self.host_exists(mac)
    result = {}
    if exists['exists']:
      result['status'] = 'Host already exists'
      result['host'] = exists['host']
    else:
      host = Host(mac=mac)
      with Session(self.engine) as session:
        session.add(host)
        session.commit()
      result['status'] = 'Success'
      result['host'] = host
    return result
  
  def find_host(self, mac):
    host = self.host_exists(mac)
    if host['exists']:
      return {'status': 'Success', 'host': self.host_to_dict(host['host'])}
    else:
      return {'status': 'Host not found'}

  def host_exists(self, mac):
    session = Session(self.engine)
    stmt = select(Host).where(Host.mac == mac) 
    host = session.scalars(stmt)
    all_hosts = host.all()
    results = {'status': 'Success', 'host': host}
    if len(all_hosts) == 0:
      results['exists'] = False
    else:
      results['host'] = all_hosts[0]
      results['exists'] = True
    return results

  def host_to_dict(self, host):
    print(host)
    return [{column.name: getattr(host, column.name) for column in Host.__table__.columns}][0]

def generate_engine(connection_uri='sqlite:///:memory:'):
  return create_engine(connection_uri, echo=True)
