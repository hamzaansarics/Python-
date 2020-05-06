
#  print(len(a))
#  print(a.count(b)) Case Senstive
a, b = input("Enter a value").split(",")
s=a.lower()
p=b.lower().strip()
print(len(s))
print(s.count(p))