# aa=lambda a,b: a+b///////// Function With Lamda Expression (anynomuios Function )////////////
# print(aa(12,10))
# print(type(aa))
# def aa(a,b): //////////////// Simple Function with Name ///////////
#      return a+b
# print(aa(10,22))
# print(type)

# a=[1,2,3,4,3]
# def a1(l):
#     return l
# print(a1(a).index(2))
# a=[1,2,3,6,8,9]
# def ec(s):
#     for i in s:
#         if i%2==0:
#            print(i,end=" ")
#         return s
# print(ec(a))
#  for i in s
# aa=lambda a:'Cool' if a>70 else 'Bad'
# print(aa(90)),

# l1=[3,2,6]
# l2=[3,6,8]
# l3=[7,99,7]
# def ae(a,k,p):
#     an=[]
#     s=0
#     l=0
#     m=0
#     for i in a:
#         s+=i
#         # l+=j
#         # m+=k
#     an.append(s/3)
#     for j in k:
#         l+=j
#     an.append(l/3)
#
#     for s in p:
#         m+=s
#     an.append(m/3)
#
#     return an
#
# print(ae(l1,l2,l3))
el=[]
el2=[]
l1=[1,2,3]
l2=[6,7,8]
def asa(a,c):
    aa=list(zip(a,c))
    n=0
    for i in aa:
        el2.append(i)
    return list(el2)

print(asa(l1,l2))

