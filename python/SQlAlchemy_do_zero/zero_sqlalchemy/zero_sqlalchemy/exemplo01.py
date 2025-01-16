import sqlalchemy as sa

metadata = sa.MetaData()

data = sa.Table(
    'comments',
    metadata,
    sa.Column('id',sa.Integer(), nullable = False),
    sa.Column('name',sa.String(), nullable = False),
    sa.Column('comment',sa.String(), nullable = False),
    sa.Column('live',sa.String(), nullable = False),
    sa.Column('created_at',sa.DateTime(), nullable = False),
    sa.PrimaryKeyConstraint('id')
)

engine = sa.create_engine('sqlite:///C:/DataPy/database.db')

metadata.create_all(engine)