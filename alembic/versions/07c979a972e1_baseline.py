"""baseline

Revision ID: 07c979a972e1
Revises:
Create Date: 2017-07-28 23:14:40.131158

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Enum
import enum

# revision identifiers, used by Alembic.
revision = '07c979a972e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass



def downgrade():
    pass
