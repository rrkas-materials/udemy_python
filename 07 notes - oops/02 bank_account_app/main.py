from account import Account
from sb import SB

if __name__ == '__main__':
    ac =  Account('balance.txt')
    print(ac.__doc__)
    # print(acc.bal)
    # acc.withdraw(100)
    # print(acc.bal)
    # acc.commit()

    #inheritence
    acc = SB('balance.txt',20)
    # print(acc.__doc__)
    acc.deposit(100)
    print(acc.bal)
    acc.commit()
    acc.calculate_1y()