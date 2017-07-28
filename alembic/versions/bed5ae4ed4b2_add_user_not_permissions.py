"""add user not permissions

Revision ID: bed5ae4ed4b2
Revises: 07c979a972e1
Create Date: 2017-07-29 01:44:20.170409

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Enum
import enum


# revision identifiers, used by Alembic.
revision = 'bed5ae4ed4b2'
down_revision = '07c979a972e1'
branch_labels = None
depends_on = None


def upgrade():
    class PT(enum.Enum):
        owner = 1
        can_edit = 2
        can_read = 3

    op.create_table(
        'user',
        Column('id', Integer, unique=True, primary_key=True),

        Column('username', String(), nullable=False, unique=True),
        Column('first_name', String()),
        Column('last_name', String()),
        Column('language', String()),

        Column('first_access', DateTime(), default=func.now()))

    op.create_table(
        'note',
        Column('id', Integer, primary_key=True, unique=True),

        Column('title', String()),
        Column('body', String()),

        Column('last_edit_date', DateTime(), default=func.now()),
        Column('last_edit_user', Integer, ForeignKey('user.id')),

        Column('previous_version', Integer, ForeignKey('note.id'), primary_key=True, nullable=True, default=None),
        Column('next_version', Integer, ForeignKey('note.id'), primary_key=True, nullable=True, default=None)
    )

    op.create_table(
        'permission',
        Column('id', Integer, primary_key=True, unique=True),

        Column('user', Integer, ForeignKey('user.id')),
        Column('note', Integer, ForeignKey('note.id')),
        Column('permission_type', Enum(PT))
    )


def downgrade():
    op.drop_table('bug')
