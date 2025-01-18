#3. Simple Banking System


menu="""
$$$$$$ Banking System $$$$$$
1.Create Account
2.Deposit Money
3.Withdraw Money
4.Check Balance
0.Exit
"""
accounts = []

def create_account():
    name=input("Enter the account name:")
    if len(accounts)!=0:
        for account in accounts:
            if account["name"]==name:
                print("Account exist with this name!!")
            else:
                account={"name":name,"balance":0}
                accounts.append(account)
                print("account created successfully!")
    else:
        account={"name":name,"balance":0}
        accounts.append(account)
        print("account created successfully!")
def deposit_money():
    name=input("Enter account name:")
    for account in accounts:
        if account["name"]==name:
            amount=int(input("Enter deposit amount:"))
            account["balance"]+=amount
            print("deposit money successfully")
        else:
            print("account not found!")

def withdraw_money():
    name=input("Enter account name:")
    for account in accounts:
        if account["name"]==name:
            amount=int(input("Enter deposit amount:"))
            if account["balance"]>=amount:
                account["balance"]-=amount
                print("deposit money successfully")
            else:
                print("You haven't enough balance!")
        else:
            print("account not found!") 
                   
def check_balance():
    name=input("Enter account name:")
    for account in accounts:
        if account["name"]==name:
           print(account["balance"])
        else:
            print("account not found!")
def main():
    try:
        while True:
            print(menu)
            option=int(input("Choose an option:"))
            if(option==1):
                create_account()
            elif (option==2):
                deposit_money()
            elif (option==3):
                withdraw_money()
            elif (option==4):
                check_balance()
            elif(option==0):
                break
            else:
                print("Invalid Input!")
    except:
        print("something went wrong!! Restart application!")

if __name__=="__main__":
    main()