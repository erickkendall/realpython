def mask(l):
  l = len(var)
  if l <= 4: return var
  return (l-4)*"#" + var[-4:]

var = input()

beg=var[:len(var)-4]
end=var[-4:]

if len(var) >= 4:
  length=len(var)-4
  str = "#" * length
  str = str + end
  print(str)
else:
  print(var)

p = mask(var)
print(p)

