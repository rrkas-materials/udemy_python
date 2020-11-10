#inheritance

from account import Account


#class child_class_name(base_class_name):
#   body


class SB(Account):                              #inheritance

    def __init__(self, filepath, charges):
        self.rate = 5
        Account.__init__(self, filepath)
        # at this point, super class members are available
        self.bal -= charges
        self.commit()

    def calculate_1y(self):
        print(self.bal * self.rate / 100)