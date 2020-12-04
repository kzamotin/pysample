import pytest
import sys 
sys.path.append('../')  
from walletClass import Wallet

@pytest.mark.smoke
def test_makeWallet():
    A=Wallet(10)
    assert A.balance() == 10

@pytest.mark.smoke
def test_makeEmptyWallet():
    A=Wallet(0)
    assert A.balance() == 0

@pytest.mark.smoke
def test_addMoney():
    A=Wallet(10)
    A.addMoney(1)
    assert A.balance() == 11

@pytest.mark.smoke
def test_makePayment():
    A=Wallet(10)
    B=Wallet(2)
    B.makePayment(A,2)
    assert B.balance() == 0


def test_makeNotEmptyWallet():
    A=Wallet(-1)
    assert A.balance() < 0


def test_makePaymentMoreThatWallet():

    A=Wallet(10)
    B=Wallet(2)
    B.makePayment(A,5)
    assert B.balance() >= 0


def test_makeWrongPayment():
    A=Wallet(10)
    B=Wallet(2)
    try:
        B.makePayment(A,'asd')

    except Exception:
        assert False

def test_makeLoopPayment():
    A=Wallet(10)
    for i in range(1,100):
        A.addMoney(1)
    assert A.balance() == 110


def test_makeLoopBackPayment():
    A=Wallet(10)
    A.makePayment(A,20)
    assert A.balance() == 10

def test_makeWrongAddMoney():
    A=Wallet(10)
    A.addMoney(-1)
    assert A.balance() == 10

@pytest.mark.parametrize("x", [10,20])
@pytest.mark.parametrize("y", [1,3,5,10])
def test_cross_params(x, y):
    A=Wallet(x)
    B=Wallet(y)
    A.makePayment(B,y)
    assert A.balance() == (x - y)
    assert B.balance() == (y + y)