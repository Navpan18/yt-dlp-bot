"""empty message

Revision ID: 63e7cae94c1d
Revises: 
Create Date: 2022-02-06 21:18:09.738831

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '63e7cae94c1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'PROCESSING', 'FAILED', 'DONE', name='taskstatus'), server_default='PENDING', nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('source', sa.Enum('API', 'BOT', name='tasksource'), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_source'), 'task', ['source'], unique=False)
    op.create_index(op.f('ix_task_status'), 'task', ['status'], unique=False)
    op.create_index('task_created_at_idx', 'task', ['created'], unique=False)
    op.create_table('file',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ext', sa.String(), nullable=True),
    sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_task_id'), 'file', ['task_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_file_task_id'), table_name='file')
    op.drop_table('file')
    op.drop_index('task_created_at_idx', table_name='task')
    op.drop_index(op.f('ix_task_status'), table_name='task')
    op.drop_index(op.f('ix_task_source'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###
