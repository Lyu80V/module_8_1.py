# def add_everything_up(a, b):
#
#     if TypeError:
#         try:
#             prim = a + b
#             return prim
#         except:
#             return str(a) + str(b)
#     else:
#         return a + b

def add_everything_up(a, b):
    try:
        prim = a + b
        return prim
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
