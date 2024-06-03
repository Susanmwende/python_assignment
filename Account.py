class Account:
    def __init__ (self,number,pin,customer_name="Susan"):
       self.number=number
       self.__pin=pin
       self.__balance = 0
       self.customer_name = customer_name
       self.__is_frozen = False
       self.__minimum_balance = None
       self.transactions = []
    def account_details(self,pin):
        if pin == self.__pin:
           print(f"your account name is {self.customer_name} and account number is {self.number}")
    def show_balance(self,pin):
        if pin==self.__pin:
         return self.__balance
        else:
             return "wrong pin"
    def deposit(self,amount):
        self.__balance += amount
        self.transactions.append(f"deposited{amount}")
        print(f"{amount} has been deposited in your account")

    

    def check_balance(self):
        print(f'Current balance:{self.__balance}')

    def change_ownership(self,new_customer_name,new_customer_id):
        self.customer_name = new_customer_name
        self.customer_id= new_customer_id
        print(f"Ownership transferred to {new_customer_name} Id number {new_customer_id}")


    def print_statement (self,pin):
        if pin == self.__pin:
            return self.transactions
        else:
            return "wrong pin"
        
    
    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)


    def overdraft_limit(self,limit):
        self.limit = limit
        print(f"Your fuliza limit is {limit}")

    def interest_calculation(self,rate,pin):
         if pin == self.__pin:
            interest_amount =self.__balance * rate /100
            self.__balance += interest_amount
            print (f"The total amount plus the intrest is {self.__balance}")
         else:
            print ("You have entered the wrong pin")
    def freeze_account(self,pin):
        if pin == self.__pin:
          self.__is_frozen = True
          print("frozen account")
        else:
            print("wrong pin")
    def unfreeze_account(self,pin):
        if pin == self.__pin:
            self.__is_frozen = False
            print("unfrozen")
        else:
            print("you have entered the wrong pin")

    def transfer_funds(self, recipient_account,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(f"withdrawal: {amount} to {recipient_account}")
            print(f"You have transferred {amount} to {recipient_account}'s account new balance is {self.__balance}")
        else:
            print("insufficient funds")
    def minimum_balance(self,mini_balance,pin):
        if pin == self.__pin:
            self.__minimum_balance = mini_balance
            print(f"Min balance requirement set to {mini_balance}")
        else:
            print("wrong pin")
    def close_account(self,pin):
        if pin == self.__pin:
            print("closed account")
        else:
            print("wrong pin")
            



    

        


        


