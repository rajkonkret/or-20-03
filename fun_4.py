# funkcje zagniezdzone
def fun():
    print("To jest fun1()")

    def fun2():
        print("To jest funkcja fun2()")

    return fun2  # bez nawiasow


xfun1 = fun()  # fun() zwraca fun2(), xfun1 zawiera funkcje, stała sie de facto funkcją
print(type(xfun1))
# skoro xFun1 zawiera funkcje, to wywołanie funkcji z nawiasami i zapisujemy xFun1()
xfun1()
