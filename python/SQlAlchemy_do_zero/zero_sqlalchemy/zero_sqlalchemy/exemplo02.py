import sqlalchemy as sa
from datetime import datetime


metadata = sa.MetaData()
engine = sa.create_engine('sqlite:///C:/DataPy/database.db')

t= sa.Table('comments',metadata,autoload_with=engine)

sql = sa.select(t) 
print(sql)

# exemplo a seguir de buildes
# stmt =  (
#     select(comments.c.name , comments.c.comment)
#     .where(comments.c.name == 'humberto luis')
#     .limit(3)
#     .offset(0)
#     .order_by(comments.c.id)
# )



# exemplo de insert 
sql_insert = (
    sa.insert(t).values(name= 'humeberto',comment = 'fazendo ultimo teste',live = '01',created_at = datetime.now())
    )

#exemplo de update 
sql_update = (
    sa.update(t)
    .where(
        t.c.name == 'humeberto'
    ).values(name = 'humberto')
)


sql = (
    sa.select(t.c.id,t.c.name,t.c.comment)
    .where(t.c.name == 'humberto')   
    .limit(3)
    .offset(2) # pular 
    .order_by(t.c.created_at)
       )


sql_delete = (
    sa.delete(t)
    .where(t.c.name ==  'isabela')
    )

with engine.connect() as con:
    result = con.execute(sql_delete)   
    con.commit()
    # print(result.fetchall())