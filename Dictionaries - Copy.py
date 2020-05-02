#///// Dictonaries //////
# dic1={'hamza':'ansai is kalowal pakisaan','ae':'21'}     ///////1st Method For Creating Dictionaries////////
# print(dic1)
# print(dic1['hamza'])
# print(dic1['ae'])
# a=dict(name='hamza',ae='21')    ///////2nd Method For Creating Dictionaries////////////
# print(a)
#
# dic1={'hamza':'ansai is kalowal pakisaan','ae':'21'}
# dic1['ae']=833
# print(dic1)
# useme= {
#     'name':'helo',
#     'ae':809809
#     }
# print(useme)

# dic1={'hamza':'ansai is kalowal pakisaan','ae':'21'}
# for i,k in dic1.items(): # /////////item Method///////// This is Power Full Method+
#    print(f"Key is {i},Value is {k}")
# for i in dic1.values(): //////Values Method /////
#     print(i)
#
# for i in dic1.keys(): ///Keys Method ////////
#     print(i)
# nas=dic1.pop('hamza')
# print(nas)
# print(dic1.clear())

# for i,k in dic1.items():
#     add=i,k
#     print(add)
# /////////// Adding Data in Dictionaries /////
# dic1['Pytohn']='I am learning second programing language'
# print(dic1)
# //////////// Pop Method in Dictionares(Deleting Item)////////////
# ass=dic1.pop('hamza')
# # print(type(ass))
# # print(dic1)    in Pop() they will return value by if str or int depeond on value

# d['name']='loe'
# print(d)

# d={
#     'name':'hamza',
#     'Email':'c@gmail.com',
#     'About':'BS In Computer Science',
#     'About': '5th Smester'
# }
# d=dict.fromkeys(['name','Email'],'khan') /////From Keys Method/////
# print(d)

# print(d['Email']) //// Access By Simple Key  /////
# print(d.get('names')) //// Access By Get() /////
# print(d.get('Abouts','Mil i'))


# print(id(d))
# d1=d.copy()
# print(d1)
# print(id(d1))
# d1=d
# print(d1 is d)
# print(id(d1))

# print(d.clear())
#
# d={'hamza':['khan','pakisan']}
# def aj(n):
#     a={}
#     for i in range(1,n+1):
#         a[i]=i**3
#     return a
# print(aj(7))
# for i,j in d:
#     print(i,j)

# aaa=[1,2,6,190,3,100]
# small=0
# for i in range(len(aaa)):

# # max=0
# # for i in range(len(aaa)):
# #     if max<=aaa[i]:
# #         max=aaa[i]
# # print(max)
# small=0
# for i in range(len(aaa)):
#     if

# a=input("Ene a no")
# s=""
# for i in range(len(a)):
#     s+=a[i]
# print(s)

# ia=input("Enter a Name")
# temp=""
# count=0
# for i in range(len(ia)-1):
#     temp=ia[i]
#     if temp[i] not in ia:
#        count+=1
#        print(temp)
#        print(count)
# temp=""
# for i in range(len(ia)-1):
#
#     if ia[i] not in temp:
#         temp+=ia[i]
#         print(f" {temp[i]} {ia.count(temp[i])}")
#
# # print(temp)
# temp=""
# def palindrome():
#     for i in range(len(ia)):
#          temp=ia
#          if temp[::-1]==ia:
#             return True
#
#     return False
# print(palindrome())

# aa=int(input("Ene a no"))
#
# def su(n):
#     a = 0
#     b = 1
#     c=0
#     if n==1:
#         print(f"{a}")
#     elif n==2:
#
#         print(f" {a},{b}  ")
#     else:
#        print(a,b,end=" ")
#        for i in range(n-2):
#          c=a+b
#          a=b
#          b=c
#          print(b, end=" ")
#
#        return ""
# print(su(aa))
#
# a=input("Enter a Name")
# def key_counter(s):
#     dictionary={}
#     for i in s:
#         dictionary[i]=s.count(i)
#     return dictionary
# print(key_counter(a))
# sa=int(input("Enter Length"))
# # for i in range(sa):
# h = input("Enter Name")
# o = input("Enter Age")
# q= input("Enter Smester").split(',')
# l = input("Enter CGPA").split(',')
# d={}
# d['Name']=h
# d['Age']=o
# d['Smester']=q
# d['CGPA']=l
# print(d.popitem())
# print(d)
# for i,j in d.items():
#     print(f"{i} : {j}")
