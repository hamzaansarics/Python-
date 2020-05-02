 # ///////////// Deocorator are Increase the functionlilty of other function////
#//// Simple Decorator //////
# They Can't Get any Parameter

# def decorator_function(any_function):
#     def incease_functionality():
#         print("This will increase the funcationality of other Function")
#         any_function()
#     return incease_functionality
#
# def simple():
#     print("This is most simple fn.")
# ka=decorator_function(simple)
# ka()

#//// Little Bit Complex Decorator ////
#Getting Paramater

# def decorotaor_function(any_func):
#        def inceasing_func(*args,**kwargs):
#         """This is Decorator Function"""
#         return any_func(*args,**kwargs)
#        return inceasing_func
# @decorotaor_function
# def add(a,c):
#     """This is Add Function"""
#     return a+c
# print(add(12,13)) #Problem! /// On Calling  Name or doc of Add Fn. they show Decocrator Data


#/// More Complex Decorator ///
#Problem Free Decorator
# from functools import wraps /// They Import Wraps Module for Fixing Real Information of Fn. whicih is called
# def dec_fn(any_func):
#     @wraps(any_func)
#     def inceae_func(*args,**kwargs):
#         """This is incsea func"""
#         return any_func(*args,**kwargs)
#     return inceae_func
# @dec_fn
# def muliply(x,z):
#     """This is Multiplyer Function"""
#     return x*z
# print(muliply(12,3))
# print(muliply.__doc__)
# print(muliply.__name__)

# from functools import wraps
# import time
# t1 = time.time()
# def print_function_data(any_function):
#
#     @wraps(any_function)
#     def increase_functionality(*args):
#         '''They will increase the functionality'''
#         return any_function(*args)
#     return increase_functionality
# @print_function_data
# def add(a,b):
#     '''They will take two arguments and simply add them together'''
#     return a+b
# print("You are calling",add.__name__,"Funcation")
# t2=time.time()
# print(t2-t1)

# from functools import wraps
# def int_allow(any_function):
#     @wraps(any_function)
#     def increase_func(*args):
#         """They Will Take only Integer as input"""
#         data=[]
#         for i in args:
#             data.append(type(i)==int)
#         if all(data):
#             return any_function(*args)
#         else:
#             print("Error! You Can't Give any List,String,Float or other")
#     return increase_func
# @int_allow
# def adding_values(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(adding_values(1,2,3))

#/// Decorator with Argument /////
# from functools import wraps
# def allow_da(dd):
#     def decoa_unc(any_unc):
#         @wraps(any_unc)
#         def incease_unc(*args):
#             EM=[]
#             for i in args:
#                 EM.append(type(i)==dd)
#             if all(EM):
#                 return any_unc(*args)
#             else:
#                 print("Invalid Argument Selected")
#         return incease_unc
#     return decoa_unc
# @allow_da(int)
# def add(*args):
#     return args
# print(add(1,2,'sd'))









