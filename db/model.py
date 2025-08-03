from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from connect import db

class Host(db.Model):
  id: Mapped[int] = mapped_column(primary_key = True)
  hostname: Mapped[str] = mapped_column(unique = True)
