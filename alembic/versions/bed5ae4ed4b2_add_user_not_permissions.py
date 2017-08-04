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
    pass


def downgrade():
    pass
