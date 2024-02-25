print("Hello KIP")
a=10
b=0
try:
    print("This is outer try block")
    try:
        print (a/b)
    except ZeroDivisionError
        print("Divisio by 0")
    finally:
        print("inside inner finnally block")

    except Exception:
        print("General Exception")
    finally:
        print("inside inner finally block")