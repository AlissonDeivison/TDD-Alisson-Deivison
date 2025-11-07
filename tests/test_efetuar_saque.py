from ..main import ContaBancaria
import pytest

def test_efetuar_saque():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    conta.sacar(500.0)
    assert conta.saldo == 500.0
    
def test_efetuar_saque_insuficiente():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    with pytest.raises(ValueError, match="Saldo insuficiente para saque"):
        conta.sacar(1500.0)

def test_efetuar_saque_zero():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    with pytest.raises(ValueError, match="Valor de saque deve ser maior que zero"):
        conta.sacar(0.0)
        
def test_efetuar_saque_valor_negativo():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    with pytest.raises(ValueError, match="Valor de saque deve ser maior que zero"):
        conta.sacar(-500.0)
