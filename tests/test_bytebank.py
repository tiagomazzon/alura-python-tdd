from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given - contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When - ação

        assert resultado == esperado # Then - desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = ' Lucas Carvalho '  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # given
        entrada_nome = 'Teste'
        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000000  # given
            entrada_nome = 'Teste'

            funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then

    # def test_retorno_str(self):
    #     entrada_nome, entrada_data_nascimento, entrada_salario = 'Teste', '10/10/1990', 1000  # given
    #     esperado = 'Funcionario(Teste, 10/10/1990, 1000)'

    #     funcionario_teste = Funcionario(entrada_nome, entrada_data_nascimento, entrada_salario)
    #     resultado = funcionario_teste.__str__()  # when

    #     assert resultado == esperado  # then