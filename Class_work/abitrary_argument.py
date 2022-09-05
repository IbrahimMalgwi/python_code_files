def func(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


func(1, 2, 3, 4, 5, 6)


# keyword argument
def func1(**kwargs):
    print(kwargs)


func1(a=1, b=2, c=3, d=4, e=5)

lst = [3, 1, 7, 4, -3, 4]
# tuple unpacking
func(*lst)

dict = {"a": 2, "b": 6, "d": 7}

func1(**dict)


def func_again(a, b, /, c, *, d):
    print(a, b, c, d)


func_again(1, 2, 3, d=4)
# def variance(*args):
#     sum(sum(args) / len(args) - args) ** 2 for arg in args) / len(args))
