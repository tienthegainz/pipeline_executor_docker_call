"""Create tables

Revision ID: 9c80c83b5711
Revises: 
Create Date: 2021-09-16 14:57:40.789690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c80c83b5711'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('process',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_image', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_process_id'), 'process', ['id'], unique=False)
    op.create_table('layer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('process_id', sa.Integer(), nullable=True),
    sa.Column('cur_image', sa.String(), nullable=False),
    sa.Column('input_params', sa.String(), nullable=True),
    sa.Column('container', sa.String(), nullable=True),
    sa.Column('next_image', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['process_id'], ['process.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_layer_id'), 'layer', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_layer_id'), table_name='layer')
    op.drop_table('layer')
    op.drop_index(op.f('ix_process_id'), table_name='process')
    op.drop_table('process')
    # ### end Alembic commands ###
