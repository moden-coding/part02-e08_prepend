#!/usr/bin/env python3

class Prepend(object):
    
    
    def __init__(self, param1):
        self.start = param1
        
    
    def write(self, s):
        print(f"{self.start}{s}")

# class MyClass(object):
#     """Documentation string of the class"""
    
    

#     def __init__(self, param1, param2):
#         "This initialises an instance of type ClassName"
#         self.b = param1 # creates an instance attribute
#         c = param2      # creates a local variable of the function
#         # statements ...
    
#     def f(self):
#         """This is a method of the class"""
#         # some statements
#         print(self.b)
    
#     a=1 # This creates a class attribute
    
def main():
    p = Prepend("+++ ")
    p.write("Hello");

if __name__ == "__main__":
    main()
