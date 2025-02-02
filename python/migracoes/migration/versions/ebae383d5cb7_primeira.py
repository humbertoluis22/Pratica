"""primeira

Revision ID: ebae383d5cb7
Revises: 
Create Date: 2025-01-16 20:44:09.250692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebae383d5cb7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id',sa.Integer(),primary_key=True,autoincrement=True),
        sa.Column('nome',sa.String(length=50),nullable=False),
        sa.Column('senha',sa.String(length=50),nullable=False)
        )


def downgrade() -> None:
    op.drop_table('pessoa')
