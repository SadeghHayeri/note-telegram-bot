from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq', start=1, increment=1), unique=True, primary_key=True)

    username = Column(String, unique=True) #TODO: fix edit username problems!
    first_name = Column(String)
    last_name = Column(String)
    language = Column(String)

    first_access = Column(DateTime, default=func.now())

    def __str__(self):
        return '%s (%s %s)' % (self.username, self.first_name, self.last_name)


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, Sequence('user_id_seq', start=1, increment=1), unique=True, primary_key=True)

    title = Column(String)
    body = Column(String, default='')

    last_edit_date = Column(DateTime, default=func.now())
    last_edit_user = Column(Integer, ForeignKey("user.id"))

    previous_version = Column(Integer, ForeignKey("note.id"), nullable=True)
    next_version = Column(Integer, ForeignKey("note.id"), nullable=True)

    def __str__(self):
        return '%s (%s)' % (self.body, self.title)


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, Sequence('user_id_seq', start=1, increment=1), unique=True, primary_key=True)

    class PT(enum.Enum):
        owner = 1
        can_edit = 2
        can_read = 3

    user = Column(Integer, ForeignKey("user.id"))
    note = Column(Integer, ForeignKey("note.id"))
    permission_type = Column(Enum(PT))
