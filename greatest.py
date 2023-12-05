from collections import Counter
var = [1,3,8,9,7,1,1,2,7,5,7,1]
results = {}

for i in range(len(var)):
  results[i]=0

for key, value in results.items():
  count=0
  for i in range(len(var)):
    if key == var[i]:
      count += 1
  results[key]=count

var.sort()
print(var)
print(results)

count=0
for key, value in results.items():
  if count == 0:
    biggest = value
  elif value >= biggest:
    biggest = value
    print(results[key])
  count += 1

print(biggest)
count=Counter(var)
print(count)
top_elems = sorted(
  count.keys(),
  key=lambda x: count[x])
