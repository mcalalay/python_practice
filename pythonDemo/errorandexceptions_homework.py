
while True:

    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter another number: "))
        z = x/y
    except ZeroDivisionError:
        print("You cannot divide a number by zero, it will render an undefined value")
        continue
    except:
        print("please enter digits only")
        continue
    else:
        print(z)
        break
    finally:
        print("keep practicing math!")