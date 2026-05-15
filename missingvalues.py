nums=list(map(int, input("Enter the numbers: ").split()))

def find(nums):
  full_range=set(range(min(nums),max(nums)+1))
  return sorted(full_range-set(nums))
  
print(find(nums))