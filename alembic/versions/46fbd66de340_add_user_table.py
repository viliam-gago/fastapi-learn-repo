"""add user table

Revision ID: 46fbd66de340
Revises: 96d2bff64625
Create Date: 2023-09-30 09:05:06.027566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46fbd66de340'
down_revision: Union[str, None] = '96d2bff64625'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("user",
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at",
               sa.TIMESTAMP(timezone=True), 
               server_default=sa.text("now()"),
               nullable=False
               ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint("email")
)


def downgrade() -> None:
    op.drop_table("user")
