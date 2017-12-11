"""empty message

Revision ID: b0f199cab531
Revises: 2c8288009690
Create Date: 2017-12-11 09:35:26.716312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0f199cab531'
down_revision = '2c8288009690'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('leave_days', sa.Integer(), nullable=True),
    sa.Column('days_present', sa.Integer(), nullable=True),
    sa.Column('percentage_attendance', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'projects', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'projects', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.drop_column(u'projects', 'employee_id')
    op.drop_table('attendances')
    # ### end Alembic commands ###