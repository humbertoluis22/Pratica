from sqlalchemy import create_engine,text

db_path = 'C:/DataPy/Casa.db' # banco q eu criei apenas para 'testes' e aprendizado

engine = create_engine( # factore # maquina de criar conexões 
    f'sqlite:///{db_path}',
    echo=True
)

con1 = engine.connect()
# print(con1.engine.url)  # mostra o caminho que o con esta utilizando para acessar o banco

# con2 = engine.connect()
# con3 = engine.connect()
# print(con)

print(engine.pool.status()) # VERIFICVA QUANTAS CONEXOES EXISTEM NO MOMENTNO # maximo 5


# print(engine)
# print(engine.dialect)

with engine.connect() as con:
    # cria um grupo de coisa para fazer varias requisições sem abrir e fechar conexao 
    # duas conexoes distintas
    # conexões atomicas -> se uma der errado as duas dao como errado 
    with con.begin():
        sql = text('select Nome  from validando') # query para rodar no banco 
        result = con.execute(sql) 
        print(result)
        print(result.fetchall()) # solicita todo o resultado da query
        print(result.fetchone()) # pega o primeira
        print(result.fetchmany(3)) #  pega alguns valores
        print(result.first()) # pega um mas nao da erro se nao conseguir
    with con.begin():
        sql = text('select Nome  from validando') # query para rodar no banco 
        result = con.execute(sql) 
pass
# con1.close() # fecha conexao 