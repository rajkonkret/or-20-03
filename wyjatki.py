def dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except TypeError:
        print("Bład typu")
    except Exception as e:
        print("Inny bład")
    else:
        print("Nie ma")
    finally:
        print("Zawsze")


print(dzielenie("a", 0))
print("Działa dalej")
print(dzielenie(2, 1))
