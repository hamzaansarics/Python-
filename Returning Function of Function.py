def outer_function(msg):
    def inner_function():
        print(f"this is inner function data {msg}")
    return inner_function
var=outer_function('this is hamza asnari')
var()













