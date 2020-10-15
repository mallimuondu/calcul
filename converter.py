def activity():
    global activity
    activity = input("""
    We are going to be convert:
    a Money
    b Measurement
    c Liquids
    d Exit program

    """)
activity()
if activity == "Money" or activity == "money" or activity == "a" or activity == "A":
    def converter():
        global what_convert
        what_convert = input("Do you want to convert a) ksh to usd or b) usd to ksh:  ")
    converter()

    if what_convert == "b":
        usd_cash = int(input("Enter how much dollars you want to convert: "))
        print("The amount you have inputed into kenya shilings = ",usd_cash * 108.59)
        def again():
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "a":   
        ksd_cash = int(input("Enter how much kenya shillings you want to convert: "))
        print("The amount you have inputed into ud dolars = ",ksd_cash / 108.59)
        def again():
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
        again()
    else:
        print("I did not understand you")
elif activity == "b":
    def whatconverting():
        global what_convert
        what_convert = input("""
        Do you want to convert
        a Km to m
        b M to km
        c M to cm
        d cm to M
        e Km to cm
        f Cm to Km
        g Go back to the top
        
        
        """)
    whatconverting()
    if what_convert == "a":
        def again():

            km = float(input("Enter the amount in km:  "))
            print("The amount in meters is ",km * 1000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                again()
            elif again == "n":
                whatconverting()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "b":
        def again():
            m = float(input("Enter the amount in m:  "))
            print("The amount in km is ",m / 1000)
            
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                again()
            elif again == "n":
                whatconverting()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "c":
        def again():
            m = float(input("Enter the amount in m:  "))
            print("The amount in centimeters is ",m * 1000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                again()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "d":
        def again():

            cm = float(input("Enter the amount in cm:  "))
            print("The amount in cm is ", cm/1000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                whatconverting()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "e":
        def again():
            km = float(input("Enter the amount in km:  "))
            print("The amount in cm is ", km*1000000)
            
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                again()
            elif again == "n":
                whatconverting()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "f":
        def again():

            cm = float(input("Enter the amount in cm:  "))
            print("The amount in km is ", cm/1000000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                again()
            elif again == "n":
                whatconverting()
            else:
                print("I did not understand you")
        again()
    elif what_convert == "g":
        activity()
elif activity == "c":

    def converter():
        global what_convert
        what_convert = input("""These are the options of converting
        a L to ml
        b ml to l
        c dl to l
        d l to dl
        e Ml to dl
        f Dl to ml
        g Go back to the top
        
         """)
    converter()
    if what_convert == "a":
        def again():
            l = int(input("Enter the amount in l:  "))
            print("The amound in ml is ",l*1000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "b":
        def again():
            ml = int(input("Enter the amount in ml:  "))
            print("The amound in l is ",ml/1000)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "c":
        def again():
            dl = int(input("Enter the amount in dl:  "))
            print("The amound in l is ",dl/10)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "d":
        def again():
            l = int(input("Enter the amount in l:  "))
            print("The amound in dl is ",l*10)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "e":
        def again():
            ml = int(input("Enter the amount in ml:  "))
            print("The amound in dl is ",ml/100)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "f":
        def again():
            dl = int(input("Enter the amount in dl:  "))
            print("The amound in ml is ",dl*10)
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
        again()
    elif what_convert == "g":
        activity()
elif activity == "d":
    print("Bye")
else:
    print("I did not understand you")
    activity()