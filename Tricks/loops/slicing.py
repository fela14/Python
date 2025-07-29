lst = [1,2,3,4,5]
print(lst)

print(lst[1:3:1])
print(lst[1:3])
print(lst[::2])
print(lst[::-1])

del lst[:]
print(lst)

orig_lst = lst
lst[:] = [7,8,9]
print(orig_lst)
print(lst)
print(orig_lst is lst)

sha_list = lst[:]
print(sha_list)
print(lst)
print(sha_list is lst)
