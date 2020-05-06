
# s.sort() /// Sorting with Built function ////
# print(s)
# ///////////// Now sorting with own Logic ////
s=[12,4,5,1,7,8,9,0,-1]
for i in range(len(s)):
   swaps=0
   for p in range(len(s)):
      if s[i] > s[p]:
         temp = s[i]
         s[i] = s[p]
         s[p] = temp
         swaps = 1
   if swaps==0:
      break
   print(s[i],end=" ")







