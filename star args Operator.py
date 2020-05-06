# def total(a,b): ///// Simple Function //////////
#     return a+b
# print(total(10,22))
# print(total(10,12,12)) //// Genrating Error Because Input is Extra than Parameters ///

# /////////////// *args Operator  /////////////
# n=int(input("Enter a value"))
# b=int(input("Enter b value"))
# c=int(input("Enter c value"))
# def unlimited_do(*args):
#     total=0
#     print(type(args))
#     for i in args:
#         # print(type(args))
#
#           total+=i
#
#     return total
# print(unlimited_do(n,b,c))

# n=int(input("Enter a value"))  ///// They Will Genrate Error if  we add aonther paramter with *args ////
# b=int(input("Enter b value"))
# c=int(input("Enter c value"))
# def unlimited_do(*args,num):
#     total=0
#     # print(type(args))
#     for i in args:
#         total+=i
#
#
#     return total
# print(unlimited_do(n,b,c))

# def unlimited_do(*args):
#     total=0
#
#     for i in args:
#         total+=i
#
#
#     return total
# lists=[1,2,3]
# print(unlimited_do(lists)) /////TypeError: unsupported operand type(s) for +=: 'int' and 'list'///////

# def unlimited_do(*args):
#     total=0
#
#     for i in args:
#         total+=i
#
#
#     return total
# lists=[1,2,3,10]
# list2=(1,2,3,4)
# print(unlimited_do(*lists,*list2)) ////////// Error Free Working Perfect Becaouse we Unpacked the list and tuple ////////////


# def tricky(num,*args):
#     a=[i**num  for i in args]
#     if args:
#         return a
#     return "Please Enter Args Values"
# print(tricky(3))
