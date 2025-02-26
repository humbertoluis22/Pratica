"""Adicionando mudanças na tabela Casa

Revision ID: 88abb4cc1274
Revises: ebae383d5cb7
Create Date: 2025-01-20 21:25:25.798167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88abb4cc1274'
down_revision: Union[str, None] = 'ebae383d5cb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validando',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.Text(), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pessoa')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoa',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=50), nullable=False),
    sa.Column('senha', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('validando')
    # ### end Alembic commands ###
