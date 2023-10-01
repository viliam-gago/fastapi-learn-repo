"""add foreign key to post table

Revision ID: cb4dbef68f7a
Revises: 46fbd66de340
Create Date: 2023-09-30 09:15:17.298872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb4dbef68f7a'
down_revision: Union[str, None] = '46fbd66de340'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts",
                           referent_table="user", local_cols=['owner_id'],
                           remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
