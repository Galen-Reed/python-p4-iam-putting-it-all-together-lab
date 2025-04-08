"""fixed migration

Revision ID: 60d7407878b2
Revises: acba11f013b4
Create Date: 2025-04-07 09:33:05.249292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d7407878b2'
down_revision = 'acba11f013b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_recipes_users_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_recipes_user_id_users'), 'users', ['user_id'], ['id'])
        batch_op.drop_column('users')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_recipes_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_recipes_users_users', 'users', ['users'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
