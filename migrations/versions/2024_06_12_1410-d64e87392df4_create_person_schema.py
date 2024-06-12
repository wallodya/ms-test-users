"""create person schema

Revision ID: d64e87392df4
Revises: 
Create Date: 2024-06-12 14:10:02.744018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd64e87392df4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE SCHEMA IF NOT EXISTS person AUTHORIZATION "srv-users";
    """)


def downgrade() -> None:
    op.execute("""
        DROP SCHEMA IF NOT EXISTS person RESTRICT;
    """)
