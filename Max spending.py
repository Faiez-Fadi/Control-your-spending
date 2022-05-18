class overspending:
    def __init__(self):
        self.max=0
        self.amount=0
        self.categories=[]
        self.shoplistcategory=[]
        self.shops=[]
        self.shoplist=[]
        self.shoplistamount=[]
        self.amountlist=[]
    def set_max(self,max):
        self.max=max
    def deposit(self,amount):
        self.amount+=amount
        self.categories.append('Deposit')
        self.amountlist.append(amount)
    def withdraw(self,amount):
        if (amount>self.amount):
            return 'Not enough funds'
        elif (self.max<0):
            return 'You spent too much'
        else:
            self.amount=self.amount-amount
            self.max=self.max-amount
            self.categories.append('Withdraw')
            self.amountlist.append(-amount)
            return 'Withdraw successfuly'
    def get_balance(self):
        return self.amount
    def transfer(self,amount,name):
        self.amount=self.amount-amount
        self.max=self.max-amount
        if (amount>self.amount):
            return 'Not enough funds'
        elif (self.max<0):
            return 'You spent too much'
        else:
            self.amountlist.append(-amount)
            self.categories.append('Transfer '+'to'+' '+str(name))
            return 'Transfer has been complete'
    def check_funds(self,amount):
        if self.amount< amount:
            return False
        else:
            return True
    def spending(self,h,name,amount):
        y=name.split()
        x=amount.split()
        total=0
        for j in range(len(x)):
            total+=int(x[j])
        self.max=self.max-total
        if (total>self.amount):
            return 'Not enough funds'
        elif (self.max<0):
            return 'You spent too much'
        else:
            self.amount=self.amount-total
            self.shoplist.append(h)
            self.shops.append(y)
            self.shoplistamount.append(x)
            self.shoplistcategory.append(h)
            self.categories.append(h)
            self.amountlist.append(-total)
            return 'Transaction successful'
    def general_receipt(self):
        print ("{0:{1}^30}".format('Spending summary', "*"))
        for i in range (len(self.categories)):
            print(self.categories[i].ljust(15),str(self.amountlist[i]).rjust(14))
        print("Total: ",self.amount)
    def category_receit(self):
        for i in range(len(self.shoplist)):
            print ("{0:{1}^30}".format(self.shoplist[i], "*"))
            for j in range(len(self.shops[i])):
                print(self.shops[i][j].ljust(15),str('-'+self.shoplistamount[i][j]).rjust(14))
            print('\n')
                
        
            
            
                
            
        

        
        
    
            
    
    
        
            
            
            
        
        
