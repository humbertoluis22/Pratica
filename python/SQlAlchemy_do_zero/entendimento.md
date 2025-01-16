
# SQLite

- é um tool de banco de dados 
- query build 
- orm 

# TOLLKIT Suporta :

- Async e Sync
- anotações de tipos de forma dinamica
- implementa a DBAPI -> api padrao para bancos de dados
- Suporte cPython e PyPy
- ORM
- Sistema de plugins
- Eventos

# entedimento geral 

- connection pooling -> varias conexoes para que seja mais rapido 
- dialect -> Faz conexoes com diversos banco como mariadb sqlite etc
- engine -> gerencia conexão  (existe dentro disso schemas )
- sql expression language -> pode fazer comando de sql com o python 
- orm -> conexao com bancos de dados relacionais  e python

# Orm

- Objeto : objeto python, como uma classe que contruimos
- relational : relacional é em relação aos bancos relacionais
- Mapper : quer dizer q é feito um mapeamento entre os metadados das 
em uma classe e cada row é relacionada a uma instancia    

# exemplos 

- no Exemplo01 é um exemplo de criaão de tabela da pior forma 
- no Exemplo03 é um exemplo de criaão de tabela  de uma forma melhor