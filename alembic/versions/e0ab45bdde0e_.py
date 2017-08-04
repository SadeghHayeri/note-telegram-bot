"""empty message

Revision ID: e0ab45bdde0e
Revises: bed5ae4ed4b2
Create Date: 2017-08-04 20:35:36.597017

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Enum
import enum


# revision identifiers, used by Alembic.
revision = 'e0ab45bdde0e'
down_revision = 'bed5ae4ed4b2'
branch_labels = None
depends_on = None

def upgrade():
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

        Column('previous_version', Integer, ForeignKey('note.id'), nullable=True, default=None),
        Column('next_version', Integer, ForeignKey('note.id'), nullable=True, default=None)
    )

    class permission_enum(enum.Enum):
        owner = 1
        can_edit = 2
        can_read = 3

    op.create_table(
        'permission',
        Column('id', Integer, primary_key=True, unique=True),

        Column('user', Integer, ForeignKey('user.id')),
        Column('note', Integer, ForeignKey('note.id')),
        Column('permission_type', Enum(permission_enum))
    )


def downgrade():
    op.drop_table('permission')
    op.drop_table('note')
    op.drop_table('user')
