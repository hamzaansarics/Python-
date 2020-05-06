# l=list(range(1*1*1,3*3*2))
# print(l)

# names=['khan','anai','hello']
# newlis=[]
# for i in names:
#     newlis.append(i[0])
# print(newlis)
# newlis=[i[0] for i in names]
# print(newlis)
# ////////////////////// Lengthy Method /////////////
# for i in range(1,10):
#     newlis.append(i)
# print(newlis)

# /////////////// List Comprehension //////////
# newlis=[i for i in range(1,11)]
# print(newlis)

# a=['khan','ansai','hamza']
# def al(l):
#    em=[]
#    em=[i[::-1] for i in l]
#    return em
# print(al(a))
a=[1,2,3,4,5,6,7]
# def Even_Checker(l):
#    EL=[]
#    for i in l:
#        if i%2==0:
#            EL.append(i)
#    return EL
# print(Even_Checker(a))

# def evch(l):
#     EL=[]
#     EL=[i for i in l if i%2==0]
#     return EL
# print(evch(a))

# EL=[i for i in range(1,11) if i%2!=0]
# print(EL)
# mixlis=[True,False,1,2.0,3,('hamza','ansai'),[1,2,3,6]]
# def filtring(l):
#     newlis=[]
#     newlis=[str(i) for i in l if type(i)!=list and type(i)!=tuple and type(i)!=bool]
#     return newlis
#
# print(filtring(mixlis))

# a=[1,2,3,6,7,8,9]
# def li(l):
#     aa=[]
#     for i in l:
#         if i%2==0:
#             aa.append(i*2)
#         else:
#             aa.append(-i)
#     return aa
# print(li(a))
newlis=[]
# newlis=[i*2 if (i%2==0) else -i for i in a]
# print(newlis)
# newlis=[[i for i in range(3)] for i in range(5)]
# # print(newlis)




