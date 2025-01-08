from sqlalchemy import create_engine,text

db_path = 'C:\DataPy\Casa' # banco q eu criei apenas para 'testes' e aprendizado

engine = create_engine( # factore
    f'sqlite:///{db_path}',
    echo=True
)

print(engine.pool)
con1 = engine.connect()
# con2 = engine.connect()
# con3 = engine.connect()
# print(con)

print(engine.pool.status()) # VERIFICVA QUANTAS CONEXOES EXISTEM NO MOMENTNO # maximo 5


# print(engine)
# print(engine.dialect)

with engine.connect() as con:
    sql = text('select Nome  from validando') # query para rodar no banco 
    result = con.execute(sql) 
    print(result)
pass
# con1.close() # fecha conexao 