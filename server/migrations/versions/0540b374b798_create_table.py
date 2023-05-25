"""create table

Revision ID: 0540b374b798
Revises: 1ae1105e6d50
Create Date: 2023-05-25 10:41:22.957849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0540b374b798'
down_revision = '1ae1105e6d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###