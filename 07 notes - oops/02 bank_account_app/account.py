class Account:                              # class
    """This class creates a new account"""  
    # appears in __doc__
    
    type = 'current'                        # class variable, shared by all instances, like static variables

    def __init__(self, filePath):           # constructor
        self.filePath = filePath            # instance variable
        with open(filePath, 'r') as file:
            self.bal = int(file.read())

    def withdraw(self, val):                # method
        self.bal -= val
    
    def deposit(self, val):
        self.bal += val

    def commit(self):
        with open(self.filePath, 'w') as file:
            file.truncate(0)
            file.write(str(self.bal))

    def ___privateMethod(self):
        print('this is a private method which is accessible only inside class.')
