"""Initial migration with updated ID fields

Revision ID: 17cf204b07e7
Revises: 
Create Date: 2024-10-20 18:26:32.746921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17cf204b07e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('lawyer',
    sa.Column('lawyer_id', sa.Integer(), nullable=False),
    sa.Column('specialization', sa.String(length=120), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('hourly_rate', sa.Float(), nullable=False),
    sa.Column('availability', sa.JSON(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('lawyer_id')
    )
    op.create_table('booking',
    sa.Column('booking_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyer.lawyer_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('booking_id')
    )
    op.create_table('review',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyer.lawyer_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    op.create_table('service',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyer.lawyer_id'], ),
    sa.PrimaryKeyConstraint('service_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('review')
    op.drop_table('booking')
    op.drop_table('lawyer')
    op.drop_table('user')
    # ### end Alembic commands ###