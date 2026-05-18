arr = [1, -2, 3, -4, 5, -6, 7, -8]

positives = [x for x in arr if x >= 0]
negatives = [x for x in arr if x < 0]

result = []

i = j = 0

while i < len(positives) and j < len(negatives):
    result.append(positives[i])
    result.append(negatives[j])
    i += 1
    j += 1

result.extend(positives[i:])
result.extend(negatives[j:])

print(result)