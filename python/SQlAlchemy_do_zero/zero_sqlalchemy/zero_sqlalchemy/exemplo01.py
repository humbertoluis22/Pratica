import sqlalchemy as sa

metadata = sa.MetaData()

# data = sa.Table(
#     'comments',
#     metadata,
#     sa.Column('id',sa.Integer(), nullable = False),
#     sa.Column('name',sa.String(), nullable = False),
#     sa.Column('comment',sa.String(), nullable = False),
#     sa.Column('live',sa.String(), nullable = False),
#     sa.Column('created_at',sa.DateTime(), nullable = False),
#     sa.PrimaryKeyConstraint('id')
# )

data = sa.Table(
    'pessoa',
    metadata,
        sa.Column('id',sa.Integer(),primary_key=True,autoincrement=True),
        sa.Column('nome',sa.String(length=50),nullable=False),
        sa.Column('email',sa.String(length=50),nullable=False)
    )



engine = sa.create_engine('sqlite:///C:/DataPy/live_migration.db')

metadata.create_all(engine)