class BankAccount:

    def __init__( self, account_number, owner, balance ):

        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = [ ]

    def add_transaction( self, description ):
            self.transactions.append( description )
            if len( self.transactions ) > 5:
                self.transactions.pop( 0 )

    def deposit( self, amount ):
            if amount >= 0:
                self.balance += amount
                self.add_transaction( f"Deposited: £ { amount }" )

            else:
                print( "Must deposit a value greater than zero. " )

    def withdraw( self, amount ):
        if amount <= 0:
            print( "Must withdraw a value greater than zero. " )

        elif amount > self.balance:
            print( "Insufficient account balance. " )

        else:
                self.balance -= amount
                self.add_transaction( f"Withdrew: £ { amount }" )

    def transfer( self, other_account, amount ):
        if amount <= 0:
            print( "Must transfer a value greater than zero. " )

        elif amount > self.balance:
            print( "Insufficient account balance. " )

        else:
            self.withdraw( amount )
            other_account.deposit( amount )
            self.add_transaction( f"Transferred: £ { amount } to { other_account.owner } ")

    def showTransactions( self ):
        if not self.transactions:
            print( "No transactions available. " )

        else:
            print( "Transaction history: " )
            for transaction in self.transactions:
                print( " ->", transaction )



name = input( "Enter your name: " )
balance = float( input( "Enter your balance: " ))
acc1 = BankAccount("123", name, balance)

while True:

    action = int( input( "What would you like to do? \n 1. Deposit \n 2. Withdraw \n 3. Transfer \n 4. View acc balance \n 5. Cancel \n-> " ) )

    if action == 1:
        dep = int( input( "Enter amount to deposit: " ) )
        acc1.deposit(dep)

    elif action == 2:
        withd = int( input( "Enter amount to withdraw: " ) )
        acc1.withdraw(withd)

    elif action == 3:

        name = input("Enter transfer account name: ")
        number = input("Enter transfer account number: ")        
        balance = float( input( "Enter transfer account balance: " ) )
        acc2 = BankAccount(number, name, balance)

        trans = int( input( "Enter amount to transfer: " ) )
        acc1.transfer(acc2, trans)

        print(f"account balance for other account after transaction: {acc2.balance}")

    elif action == 4:
        print( acc1.balance )

    elif action == 5:
        acc1.showTransactions( )
        print( "Goodbye! " )
        break

    else:
        print ( "Incorrect input. " )

