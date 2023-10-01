"""create content column to posts table

Revision ID: 96d2bff64625
Revises: 689f56de6444
Create Date: 2023-09-30 09:00:36.107321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96d2bff64625'
down_revision: Union[str, None] = '689f56de6444'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
