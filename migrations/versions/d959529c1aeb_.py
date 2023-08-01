"""empty message

Revision ID: d959529c1aeb
Revises: a09f0f9da963
Create Date: 2023-07-28 09:50:20.433544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd959529c1aeb'
down_revision = 'a09f0f9da963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('height', sa.String(length=250), nullable=True),
    sa.Column('birth', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('eyes', sa.String(length=250), nullable=False),
    sa.Column('hair', sa.String(length=250), nullable=False),
    sa.Column('weight', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###