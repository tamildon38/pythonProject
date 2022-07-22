try:
    length=10
    width=0
    length/width
except Exception:
      print("divistion is eror change the input")


try:
    length=10
    length/width
except NameError:
     print("variable has been used before defining it")
except ZeroDivisionError:
    print("division by zero is invalied kindly change ur input")
except Exception:
    print("new error has occured")
finally:
    print("i will be exceuted atlest once")


