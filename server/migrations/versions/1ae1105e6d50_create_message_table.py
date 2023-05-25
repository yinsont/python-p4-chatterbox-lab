"""Create Message Table

Revision ID: 1ae1105e6d50
Revises: 8b3d88fd4c25
Create Date: 2023-05-25 10:37:43.921629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ae1105e6d50'
down_revision = '8b3d88fd4c25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('username', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('username')
        batch_op.drop_column('body')

    # ### end Alembic commands ###
