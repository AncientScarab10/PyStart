# def simple(a, b, *args, **kwargs):
#     print('a', a)
#     print('b', b)
#     print('args', args)
#     print('kwargs', kwargs)

# simple(1, 2, 4, 6, 10, x=1, y=3)


def sum_it(*args, limit:int=0) -> int:
    total = 0
    for arg in args:
        if arg > limit:
            total += arg
    
    return total

print(sum_it(5, 10, 15, 25, limit=6))