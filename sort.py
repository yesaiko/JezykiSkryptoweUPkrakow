list_to_sort = [[3, 2, 3], [2, 0 ,2], [3, 0 ,1]]

list_to_sort.sort(key=lambda x: (x[1], x[2]))

print(list_to_sort)