"""add_pgvector_extension

Revision ID: a81c2f01ea14
Revises: ece0918d6fee
Create Date: 2026-07-14 15:02:14.531255

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'a81c2f01ea14'
down_revision: Union[str, Sequence[str], None] = 'ece0918d6fee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.execute(
        "CREATE EXTENSION IF NOT EXISTS vector;"
    )


def downgrade():

    op.execute(
        "DROP EXTENSION IF EXISTS vector;"
    )
