def number():
    a = True
    while a == True:
        try:
            number = float(input("Enter your number:  "))
            divisibility_number = float(input("Enter your divisibility number:  "))
            calculations = number % divisibility_number
            if calculations == 0:
                print("The number is divisible")
                def again_func():
                    global again
                    again = input("Do you want to try again Yes(y) or No(n):  ")
                    if again == "y" or again == "yes" or again == "Y" or again == "Yes":
                        pass
                    elif again == "n" or again == "no" or again == "N" or again == "No":
                        print("Good bye")
                        a = False
                    else:
                        print("I did not understand you")
                        again_func()
                again_func()
            else:
                print("The number is not dividible")
                def again_func():
                    global again
                    again = input("Do you want to try again Yes(y) or No(n):  ")
                    if again == "y" or again == "yes" or again == "Y" or again == "Yes":
                        pass
                    elif again == "n" or again == "no" or again == "N" or again == "No":
                        print("Good bye")
                        a = False
                    else:
                        print("I did not understand you")
                        again_func()
                again_func()
                
        except ValueError:
            print("Pls input a number or a number with a decimal")