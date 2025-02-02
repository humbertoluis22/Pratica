# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Table, Text,String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Casa(Base):
    __tablename__ = 'validando'

    id = Column(Integer, primary_key=True)  # Coluna de chave primária
    nome = Column(Text, nullable=True)  # Nome com tipo Text
    idade = Column(Integer, nullable=True)  # Idade com tipo Integer
    email = Column(String(length=50), nullable=False)
# 



class Casa(Base):
    __tablename__ = 'validando1'

    id = Column(Integer, primary_key=True)  # Coluna de chave primária
    nome = Column(Text, nullable=True)  # Nome com tipo Text
    idade = Column(Integer, nullable=True)  # Idade com tipo Integer
    email = Column(String(length=50), nullable=False)
    senha = Column(String(length=50), nullable=False)
# 