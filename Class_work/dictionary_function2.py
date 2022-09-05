def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}

    for item in iterable:
        # if item in item_dict:
        #     item_dict[item] += 1
        # else:
        #     item_dict[item] = 1
        # ==========================================
        # item_dict[item] = item_dict.get(item, 0) + 1
        # ==========================================
        item_dict[item] = iterable.count(item)
    return item_dict


print(counter("missisipi"))


def counter2(iterable: list | str | tuple) -> dict:
    from collections import Counter
    return dict(counter(iterable))


print(counter2("hello"))


def counter3(iterable: list | str | tuple) -> dict:
    from collections import Counter, defaultdict
    item_dict = defaultdict(int)
    for item in iterable:
        item_dict[item] += 1

    return dict(item_dict)


print(counter3("monkey"))
