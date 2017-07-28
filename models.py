from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, unique=True, primary_key=True)

    username = Column(String, unique=True) #TODO: fix edit username problems!
    first_name = Column(String)
    last_name = Column(String)
    language = Column(String)

    first_access = Column(DateTime, default=func.now())


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, unique=True, primary_key=True)

    title = Column(String)
    body = Column(String)

    last_edit_date = Column(DateTime, default=func.now())
    last_edit_user = Column(Integer, ForeignKey("user.id"))

    previous_version = Column(Integer, ForeignKey("note.id"), primary_key=True, nullable=True, default=None)
    next_version = Column(Integer, ForeignKey("note.id"), primary_key=True, nullable=True, default=None)


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, unique=True, primary_key=True)

    class PT(enum.Enum):
        owner = 1
        can_edit = 2
        can_read = 3

    user = Column(Integer, ForeignKey("user.id"))
    note = Column(Integer, ForeignKey("note.id"))
    permission_type = Column(Enum(PT))