# para utilizar as funções do arquivo criado em version
    - primeiro criar o esquema do projeto 
        - alembic init <nome projeto >
    - segundo criar o arquivo no version 
        - alembic revision -m <nome>
    - rodar função updgrade
        - alembic upgrade head
    - rodar downgrade 
        - alembic downgrade base
    
    - alembic history
        -  historico de migrações