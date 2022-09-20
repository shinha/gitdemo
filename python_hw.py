def is_consecutive(a_list):
    r_list = list(range(min(a_list), max(a_list)+1)) # fix block to change depending on argument
    if a_list == r_list:
        print(f"{a_list} is consecutive numerically.")
    else:
        print(f"{a_list} is non-consecutive numerically.")
    
print('hi')
is_consecutive([1,2,3,5,4])
print('hello')

print("hello_from_brandt")

print("hello_from_carla_carney")
print("hello_from_chris")
print(f"Whaddup, it's Diante!")
