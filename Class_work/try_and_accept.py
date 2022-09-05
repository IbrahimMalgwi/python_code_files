def add(a: float, b: float) -> float | None:
    try:
        # c = a + 'b'
        a / b
    except ZeroDivisionError:
        print("Can't divide with zero")
        return None
    except (TypeError, NameError):
        print("Type error")


print(add(1, 0))
