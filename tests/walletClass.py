class Wallet(object):
    def __init__(self, amount):
        self.__amount = amount if amount>0 else 0
    
    def addMoney(self, amount):
        self.__amount += amount

    def makePayment(self, wallet, amount):
        self.__amount -= amount
        wallet.addMoney(amount)
    
    def balance(self):
        return self.__amount


A=Wallet(10)
B=Wallet(-10)
B.makePayment(A,5)
print(A.balance(), B.balance())