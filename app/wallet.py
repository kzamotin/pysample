"""
Wallet class
"""


class Wallet(object):
    """
    The Wallet class
    """
    def __init__(self, amount):
        """
        Initialisation of wallet amount
        :param amount:
        """
        self.__amount = amount if amount > 0 else 0

    def add_money(self, amount):
        """
        Add some money to wallet
        :param amount:
        :return:
        """
        self.__amount += amount

    def make_payment(self, wallet, amount):
        """
        Make payment from wallet to wallet
        :param wallet:
        :param amount:
        :return:
        """
        self.__amount -= amount
        wallet.add_money(amount)

    def balance(self):
        """
        Method for know the wallet balance
        :return:
        """
        return self.__amount
