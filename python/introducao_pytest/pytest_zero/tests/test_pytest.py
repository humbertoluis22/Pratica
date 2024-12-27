from pytest import mark
from pytest_zero.jogo import brincadeira , brincadeira2


def test_quando_brincadeira_receber_1_entao_retornar_1():
    entrada = 1  # dado
    esperado = 1  # dado
    resultado = brincadeira(entrada) #quando
    assert resultado == esperado # entao


def test_quando_brincadeira_receber_2_entao_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_retornar_queijo():
    assert brincadeira(3) == 'queijo' 


@mark.smoke
def test_quando_brincadeira_receber_5_entao_retornar_goiabada():
    assert brincadeira(5) == 'goiabada' 

@mark.smoke
def test_quando_brincadeira_receber_10_entao_retornar_goiabada():
    assert brincadeira(10) == 'goiabada' 

@mark.goiabada
@mark.smoke  
def test_quando_brincadeira_receber_20_entao_retornar_goiabada():
    assert brincadeira(20) == 'goiabada' 


@mark.skip(reason = 'vai falhar pq ainda nao implementei o meu teste')
def test_quando_brincadeira_receber_0_entao_retornar_none():
    assert brincadeira(0) == 'goiabada' 


@mark.parametrizado
@mark.parametrize(
        'entrada',
        [5,10,20,25,35]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == 'goiabada'


@mark.queijo
@mark.parametrize(
        'entrada',
        [3,6,9,12,15]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == 'queijo'


@mark.brincadeira
@mark.parametrize(
        'entrada,esperado',
        [(1,1),(2,2),(3,'queijo'),(4,4),(5,'goiabada')]
)
def test_brincadeira_deve_retornar_esperado_com_entrada(entrada,esperado):
    assert brincadeira(entrada) == esperado


@mark.xfail
def test_1brincadeira_deve_retornar_4_se_receber_4():
    assert brincadeira(4) == "queijo"


import sys
@mark.xfail(sys.platform =='win32') # esperado que falhe no sistema operacional windows
def test_2brincadeira_deve_retornar_4_se_receber_4():
    assert brincadeira(4) != "queijo"

import sys
@mark.skipif(sys.platform =='win32') # esperado que falhe no sistema operacional windows
def test_2brincadeira_deve_retornar_4_se_receber_4():
    assert brincadeira(4) != "queijo"


@mark.stdout
def test_brincadeira2_deve_imprimir_entrei_na_brincaideira(capsys):
    brincadeira2()
    resultado = capsys.readouterr()
    assert resultado.out == 'entrei na brincadeira !!\n'
    ...