"""Initial Migration

Revision ID: 5a01a79b44bf
Revises: 
Create Date: 2023-01-07 19:35:04.759003

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5a01a79b44bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('goals_achieved', sa.Integer(), nullable=True),
    sa.Column('register_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)
    op.create_table('goals',
    sa.Column('goal_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('expired_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('timeunits',
    sa.Column('timeunit_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('goal_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('info', sa.String(length=100), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.goal_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('timeunit_id')
    )
    op.create_index(op.f('ix_timeunits_timeunit_id'), 'timeunits', ['timeunit_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_timeunits_timeunit_id'), table_name='timeunits')
    op.drop_table('timeunits')
    op.drop_table('goals')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###