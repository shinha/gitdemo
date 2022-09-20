def is_consecutive(a_list):
    r_list = list(range(min(a_list), max(a_list)+1)) # fix block to change depending on argument
    if a_list == r_list:
        print(f"{a_list} is consecutive numerically.")
    else:
        print(f"{a_list} is non-consecutive numerically.")


is_consecutive([1,2,3,5,4])