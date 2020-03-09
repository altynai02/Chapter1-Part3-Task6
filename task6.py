# 6. Напишите функцию которая подсчитает количество
# счетных и несчетных чисел в списке чисел.

def even_odd(list_):
    even = 0
    odd = 0
    # list_ = input("Enter a list: ")
    for i in list_:
        if i % 2 == 0:
            even+=1
        else:
            odd += 1
    return list_, even, odd



print(even_odd([3,3,7,9]))