from pytest import mark
from pytest_zero.jogo import brincadeira 


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