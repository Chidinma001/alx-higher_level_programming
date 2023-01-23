#!/src/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    prod = 0
    wt = 0
    for ele in my_list:
        prod += (ele[0] * ele[1])
        wt += ele[1]
    return (prod / wt)
