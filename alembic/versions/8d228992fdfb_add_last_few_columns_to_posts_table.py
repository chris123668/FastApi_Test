"""add last few columns to posts table

Revision ID: 8d228992fdfb
Revises: f823843a6b27
Create Date: 2024-10-28 20:26:21.947727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d228992fdfb'
down_revision: Union[str, None] = 'f823843a6b27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    pass


def downgrade() -> None:
    op.drop_column('post', "published")
    op.drop_column('post', "created_at")
    pass
