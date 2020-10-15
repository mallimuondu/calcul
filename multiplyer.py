def multiply():
    c = True
    while c == True:
        try:
            num1 = float(input("Enter your first number:  "))
            num2 = float(input("Enter your second number:  "))
            print("The multiplication is ",num1*num2)
            def again_funct():
                global again
                again = input("Do you want to try again. Yes(y) or No(n)?  ")
            again_funct()
            if again == "y" or again == "Y" or again == "yes" or again == "Y":
                pass
            elif again == "n" or again == "N" or again == "no" or again == "No":
                print("Good")
                c = False
            else:
                print("I did not understand you")
                again_funct()
        except ValueError:  
            print("Pls input a number or a number with a decimal")
multiply()