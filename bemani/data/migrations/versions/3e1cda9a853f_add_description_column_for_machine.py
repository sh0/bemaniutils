"""Add description column for machine.

Revision ID: 3e1cda9a853f
Revises: 26dcace5d5d4
Create Date: 2017-01-03 23:19:47.702107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1cda9a853f'
down_revision = '26dcace5d5d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine', sa.Column('description', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('machine', 'description')
    # ### end Alembic commands ###
