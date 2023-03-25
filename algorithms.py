
# time complexity is O(1)
def function(n):
    if (n % 2) == 0:
        return True
    else:
        return False
        
print(function(2))


# time complexity is O(n)
def function_list(x):
    i = 0
    while i < len(x):
        n = x[i]
        if n < 100:
            i += 1
        else:
            return False
    return True
        
print(function_list([24, 58, 44, 6, 88]))


# time complexity is O(1)
def has_duplicates(x):
    if len(x) != len(set(x)):
        return True
    else:
        return False

print(has_duplicates(["Matthew", "Mark", "John", "Luke", "John"]))

# time complexity is O(n)
def sort_list(arr):
    x = []
    while arr:
        m = min(arr)
        arr.remove(m)
        x.append(m)
    return x

unsorted = [1,4,3,2,5,0]
sorted = sort_list(unsorted)
print(sorted)