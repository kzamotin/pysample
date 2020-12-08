"""
Basic auto tests wor wallet functionality
"""

import pytest
from wallet import Wallet


@pytest.mark.smoke
def test_make_wallet():
    """
    Simple wallet initialization
    """
    test_wallet = Wallet(10)
    assert test_wallet.balance() == 10


@pytest.mark.smoke
def test_make_empty_wallet():
    """
    Empty wallet test
    """
    test_wallet = Wallet(0)
    assert test_wallet.balance() == 0


@pytest.mark.smoke
def test_add_money():
    """
    Add minimum of funds to wallet
    """
    test_wallet = Wallet(10)
    test_wallet.add_money(1)
    assert test_wallet.balance() == 11


@pytest.mark.smoke
def test_make_payment():
    """
    Make simple transaction
    """
    first_wallet = Wallet(10)
    second_wallet = Wallet(2)
    second_wallet.make_payment(first_wallet, 2)
    assert second_wallet.balance() == 0


def test_make_not_empty_wallet():
    """
    Make wallet by negative of funds amount
    """
    test_wallet = Wallet(-1)
    assert test_wallet.balance() >= 0


@pytest.mark.xfail
def test_make_payment_more_that_wallet():
    """
    Wrong payment value more that wallet balance
    """
    first_wallet = Wallet(10)
    second_wallet = Wallet(2)
    second_wallet.make_payment(first_wallet, 5)
    assert second_wallet.balance() >= 0


@pytest.mark.xfail
def test_make_wrong_payment_amount():
    """
    Wrong argument for payment method
    """
    first_wallet = Wallet(10)
    second_wallet = Wallet(2)
    try:
        second_wallet.make_payment(first_wallet, 'asd')

    except Exception:
        assert False



TEST_DATA = [
    (15, 10, 0, 10),
    (15, 5, 1, 6)
]


@pytest.mark.parametrize("wallet_a, amount, wallet_b, expected", TEST_DATA)
def test_make_some_transfer(wallet_a, amount, wallet_b, expected):
    """
    Method for transfer money tests
    First wallet amount
    Transfer amount
    Second wallet initial value
    Expected second wallet amount
    """
    first_wallet = Wallet(wallet_a)
    second_wallet = Wallet(wallet_b)
    first_wallet.make_payment(second_wallet, amount)
    assert second_wallet.balance() == expected


@pytest.mark.parametrize("count", [10, 20])
def test_make_loop_payment(count):
    """
    Loop of transactions
    """
    test_wallet = Wallet(10)
    for i in range(count):
        test_wallet.add_money(1)
    assert test_wallet.balance() == 10 + count


def test_make_loop_back_payment():
    """
    Money transfer from wallet to the same wallet
    """
    test_wallet = Wallet(10)
    test_wallet.make_payment(test_wallet, 20)
    assert test_wallet.balance() == 10


@pytest.mark.xfail
def test_make_wrong_add_money_parameter():
    """
    Payment with negative amount
    """
    test_wallet = Wallet(10)
    test_wallet.add_money(-1)
    assert test_wallet.balance() == 10


@pytest.mark.parametrize("wallet_a", [10, 20])
@pytest.mark.parametrize("wallet_b", [1, 3, 5, 10])
def test_cross_params(wallet_a, wallet_b):
    """
    Cross-test of payment method for several test data sets
    """
    first_wallet = Wallet(wallet_a)
    second_wallet = Wallet(wallet_b)
    first_wallet.make_payment(second_wallet, wallet_b)
    assert first_wallet.balance() == (wallet_a - wallet_b)
    assert second_wallet.balance() == (wallet_b + wallet_b)
