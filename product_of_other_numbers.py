"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.
"""
x = [2, 7, 3, 4]

def get_products_of_all_ints_except_at_index(x):

    products_of_all_ints_except_index = [None] * len(x)

    # before index
    product_so_far = 1
    i = 0
    while i < len(x):
        products_of_all_ints_except_index[i] = product_so_far
        product_so_far *= x[i]
        print(products_of_all_ints_except_index)
        i += 1

    print('\n')
    # after index
    product_so_far = 1
    i = len(x) - 1
    while i >= 0:
        products_of_all_ints_except_index[i] *= product_so_far
        product_so_far *= x[i]
        print(products_of_all_ints_except_index)
        i -= 1

    return products_of_all_ints_except_index

print(get_products_of_all_ints_except_at_index(x))
