"""empty message

Revision ID: 2d82d0abb377
Revises: 
Create Date: 2023-07-19 20:27:07.091858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d82d0abb377'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_character', sa.Integer(), nullable=True),
    sa.Column('user_planet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_character'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_planet'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
