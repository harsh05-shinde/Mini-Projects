#using if else statement

print("welcome to ATM")
transaction_history = []
total_amount = 0
pin = int(input("Please Enter Your Pin:"))
if pin==1234:
 while True:
   print("welcome to ATM")
   print("1.Check Balance")
   print("2.Deposite")
   print("3.withdraw")
   print("4.Transaction History")
   choice  = int(input("Enter your choices: "))
   if choice==1:
    print(f"Your current amount is {total_amount}")

   elif choice==2:
      deposite = int(input("Enter Your deposite Amount:"))
      if deposite<0:
        print("Please enter Correct amount")
      else:
       total_amount = total_amount + deposite
       transaction_history.append(f"Deposited RS{deposite}")
       print(f"Now Your total amount is {total_amount}")

   elif choice==3:
       withdraw  = int(input("Please enter Your withdraw Amount:"))
  
       if withdraw>total_amount:
        print("Insufficient Fund")
       else:
        total_amount = total_amount-withdraw
        transaction_history.append(f"withdraw RS{withdraw}")
        print(f"Now Your total amount is {total_amount}")
    
   elif choice == 4:
      if transaction_history:
        for i, n in enumerate(transaction_history, start=1):
            print(i, n)
      else:
        print("No transaction History")  
   else:
    print("Please enter correct choice")
else:
 print("PLease enter correct pin")