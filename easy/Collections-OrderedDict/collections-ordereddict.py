from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    items = OrderedDict()

    for _ in range(n):
        line = input().split()
        name = " ".join(line[:-1])
        price = int(line[-1])

        if name in items:
            items[name] += price
        else:
            items[name] = price

    for name, total in items.items():
        print(name, total)
