bank=int(input("enter your amount:"))
if bank>0:
    print("account is open")
    choice=int(input("enter your choice:"))
    print("enter 1(for deposit)")
    print("enter 2(for withdrow)")
    if choice==1 :
        a=int(input("enter a amount to deposit:" ))
        bank +=a
        print(f"this new amount{bank}")
    elif choice==2:
        b=int(input("enter a amount to withdrow"))
        bank -=b
        print(f"this amount {bank}")  
    else:
        print("invalid number")  
else:
    print("account is close")

     
    