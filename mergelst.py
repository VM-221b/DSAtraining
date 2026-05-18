lst1 = list(map(int, input("Enter sorted numbers for list1: ").split()))
lst2 = list(map(int, input("Enter sorted numbers for list2: ").split()))

merged = []

i = 0
j = 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

while i < len(lst1):
    merged.append(lst1[i])
    i += 1

while j < len(lst2):
    merged.append(lst2[j])
    j += 1

print("Merged list:", merged)