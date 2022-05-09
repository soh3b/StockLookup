tick = input("Enter a symbol: ")
verified = False
while verified == False:
    for v in tick.split():
        if v.isdigit():
            print("This is not a valid symbol please try again")
            tick = input("Enter a symbol: ")
            
            
        else: verified = True