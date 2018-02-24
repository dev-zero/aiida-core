"""base_data_plugin_type_string

Revision ID: 0aebbeab274d
Revises: 35d4ee9a1b0e
Create Date: 2018-02-24 20:12:44.731358

"""
from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '0aebbeab274d'
down_revision = '35d4ee9a1b0e'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()

    # The base Data types Bool, Float, Int and Str have been moved in the source code, which means that their
    # module path changes, which determines the plugin type string which is stored in the databse.
    # The type string now will have a type string prefix that is unique to each sub type.
    statement = text("""
        UPDATE db_dbnode SET type = 'data.bool.Bool.' WHERE type = 'data.base.Bool.';
        UPDATE db_dbnode SET type = 'data.float.Float.' WHERE type = 'data.base.Float.';
        UPDATE db_dbnode SET type = 'data.int.Int.' WHERE type = 'data.base.Int.';
        UPDATE db_dbnode SET type = 'data.str.Str.' WHERE type = 'data.base.Str.';
    """)
    conn.execute(statement)


def downgrade():
    conn = op.get_bind()

    statement = text("""
        UPDATE db_dbnode SET type = 'data.base.Bool.' WHERE type = 'data.bool.Bool.';
        UPDATE db_dbnode SET type = 'data.base.Float.' WHERE type = 'data.float.Float.';
        UPDATE db_dbnode SET type = 'data.base.Int.' WHERE type = 'data.int.Int.';
        UPDATE db_dbnode SET type = 'data.base.Str.' WHERE type = 'data.str.Str.';
    """)
    conn.execute(statement)
