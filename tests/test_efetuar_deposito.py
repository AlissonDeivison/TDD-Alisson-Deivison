from ..main import ContaBancaria
import pytest

def test_efetuar_deposito():
    conta = ContaBancaria(12345, "Alisson Deivison", 0)
    conta.depositar(1000.0)
    assert conta.saldo == 1000.0

def test_efetuar_deposito_zero():
    conta = ContaBancaria(12345, "Alisson Deivison", 0)
    with pytest.raises(ValueError, match="Valor de depósito deve ser maior que zero"):
        conta.depositar(0.0)
        
def test_efetuar_deposito_valor_negativo():
    conta = ContaBancaria(12345, "Alisson Deivison", 0)
    with pytest.raises(ValueError, match="Valor de depósito deve ser maior que zero"):
        conta.depositar(-1000.0)
