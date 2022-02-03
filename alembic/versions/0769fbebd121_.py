"""empty message

Revision ID: 0769fbebd121
Revises: 63e7cae94c1d
Create Date: 2022-02-18 23:34:39.587248

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0769fbebd121'
down_revision = '63e7cae94c1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('message_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'message_id')
    # ### end Alembic commands ###
