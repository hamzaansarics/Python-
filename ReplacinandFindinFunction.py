
a="ohis is hamza ansai is o kalowal is"
# print(a.replace("is","now",1))
s=a.find("is")
sj=a.find("is",s+1)
o=a.find("is",sj+1)
print(a.find("is",o+1))