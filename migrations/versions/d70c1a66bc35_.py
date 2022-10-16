"""empty message

Revision ID: d70c1a66bc35
Revises: 880559e6bc47
Create Date: 2022-10-03 14:23:20.764020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70c1a66bc35'
down_revision = '880559e6bc47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('pict_file', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'pict_file')
    # ### end Alembic commands ###
