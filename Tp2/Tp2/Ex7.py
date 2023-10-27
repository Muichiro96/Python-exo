List = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8, 8, 2, 2, 1, 1]

l = len(List)
i = 0
j = 1
while i < l - 1:
    while j < l:
        if List[i] == List[j]:
            del List[j]
            l = l - 1
            j = j - 1
        j = j + 1
    i = i + 1
    j = i + 1
for element in List:
    print(element, end=" ")
