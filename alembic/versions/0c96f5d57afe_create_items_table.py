"""create items table

Revision ID: 0c96f5d57afe
Revises: e5467b78d2a0
Create Date: 2023-02-19 02:29:29.348094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c96f5d57afe'
down_revision = 'e5467b78d2a0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'items',
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("title", sa.String(255), nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("owner_id", sa.UUID(as_uuid=True), nullable=False)
    )
    op.create_foreign_key("fk_items_user", "items", "users", ["owner_id"], ["id"])


def downgrade() -> None:
    op.drop_table('items')
