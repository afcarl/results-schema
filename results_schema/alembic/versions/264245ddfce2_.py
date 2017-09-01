"""empty message

Revision ID: 264245ddfce2
Revises: 0d44655e35fd
Create Date: 2017-09-01 14:26:01.107455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264245ddfce2'
down_revision = '0d44655e35fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('individual_importances', sa.Column('feature_value', sa.Float(), nullable=True), schema='results')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('individual_importances', 'feature_value', schema='results')
    # ### end Alembic commands ###