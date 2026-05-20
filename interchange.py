from itertools import permutations

def find_greater_permutation(a, b):
    digits = list(str(a))
    
    perms = set(permutations(digits))
    
    valid_numbers = []
    
    for p in perms:
        num = int("".join(p))
        
        if num > b:
            valid_numbers.append(num)
    
    return min(valid_numbers) if valid_numbers else -1

a = int(input("Enter 1st no (a): "))
b = int(input("Enter 2nd no (b): "))

print(find_greater_permutation(a, b))