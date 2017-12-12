"""empty message

Revision ID: 2220462d93e4
Revises: de3e10dcb01d
Create Date: 2017-12-12 07:19:47.468766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2220462d93e4'
down_revision = 'de3e10dcb01d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subprojects', sa.Column('sp_project_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subprojects', 'projects', ['sp_project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subprojects', type_='foreignkey')
    op.drop_column('subprojects', 'sp_project_id')
    # ### end Alembic commands ###
