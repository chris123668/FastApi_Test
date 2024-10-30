"""add posts table

Revision ID: 62e91c0dea30
Revises: 4137ff016620
Create Date: 2024-10-28 20:14:46.626694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62e91c0dea30'
down_revision: Union[str, None] = '4137ff016620'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", 
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False), 
                    sa.Column('Content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")

    pass
