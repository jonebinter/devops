import time
print("Please insert your card")
time.sleep(5)
Trials = 3
UserPin = 1234
balance = 20000
while Trials != 0:
    Pin = int(input("Please Enter Your 4 digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong Pin Number, You have " + str(Trials) + " Trials left")
    else:
        print("""
                                            1==Balance enquiry
                                            2==Withdraw 
                                            3==Deposit
                                            4==Exit """
              )
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("please enter your valid choice")
        if option == 1:
            print(f"Your current balance is {balance}")
            UserExit = input("Would you like to make another transaction? Y/N: ")
            if UserExit == "N":
                print("Thank you for banking with us")
                break
            else:
                continue
        if option == 2:
            withdraw_amount = int(input("please enter withdraw amount: "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} has been debited from your account")
            print(f"your updated current balance is {balance}")
            UserExit = input("Would you like to make another transaction? Y/N: ")
            if UserExit == "N":
                print("Thank you for banking with us")
                break
            else:
                continue
        if option == 3:
            deposit_amount = int(input("please enter deposit amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} has been added to your account")
            print(f"your updated current balance is {balance}")
            UserExit = input("Would you like to make another transaction? Y/N: ")
            if UserExit == "N":
                print("Thank you for banking with us")
                break
            else:
                continue
        if option == 4:
            UserExit = input("Would you like to make another transaction? Y/N: ")
            if UserExit == "N":
                print("Thank you for banking with us")
                break
            else:
                continue
