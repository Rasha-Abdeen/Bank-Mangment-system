from add_account import Newaccount
print ('***********Welcome*************')
print ('***********BANK MANGMENT SYSTEM *************')
print ('                    Main Main')
print('1- New Account \n 2- Deposit Amount \n 3- Withdraw Amount \n 4- Balance Enquire \n 5- All Acount Holder List \n 6- Close An Account \n 7- Modify an account \n')
x = int(input('please select an option:'))
if (x == 1):
    num= int(input('Enter Account Number:\n'))
    name= input('Enter The Holder Name :\n')
    type= input('Enter the type of account (c/S):\n')
    amount = input('Enter the inital amount (>500 for saving and >=1000 for current)')
    account=Newaccount(num,name,type,amount)
    Newaccount.useraccount(account)
