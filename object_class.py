class Budget:
    
    def __init__ (self, category ):
        self.category = category
        self.amount = 0
        
    def deposit(self,amount,description = ""):
        depo = self.amount + amount
        print(f"You deposited the sum of NGN {depo} in the account.")
        
        
    def withdrawal (self,amount):
        if  amount > self.amount :
            print (f"Balance is {self.amount}, you cannot withdraw.")
        else:
            withdraw = self.amount - amount
            print (f"Your balance is NGN {withdraw}.")
            
            
    def category_bal(self):
        balance =  self.depo + self.amount - self.withdrawal
        return balance
    
    def transfer_balance(self):
        pass

