'''
Python decorator: allow us to modify or extend the behaviour of functions and methods without changing their actual code. When we use a a Python decorator, we wrap a function with another function, which takes the original function as an argument and returns its modified version. This techniques provides a siple way to implement higher-order functions in Python, enhanching code reusability and readability.

'''

# A function returns a value based on the given arguments.
def add_one(number):
    return number + 1

# print(add_one(2))

# Python treats function as first-class objects which means the function can be passed around and used as arguments just like any other object like str, int, float, list and so on. 
# Example below:

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

# say_hello() and be_awesome() are regular functions that expect a name given as a string. 

def greet_bob(greeter_func):
    return greeter_func("Bob")

# print(say_hello("Netra"))
# print(be_awesome("Name"))
print(greet_bob(say_hello)) # this say_hello function is named without parenthesis. This mean that only a reference to the function is passed. The function is not executed. The greet_bob() function, on the other hand, is written with parentheses, so it will be called as usual.
print(greet_bob(be_awesome))

'''
Note: A function name without parenthesis is a reference to a function, while a function name with trailing parenthesis calls the function and refers to its return value. 
'''


# Inner functions. 
# - It is possible to define functions inside other functions. such functions are called inner functions. Here's an example of a function with two inner functions: 
print("\n------------------ Inner functions ----------------------")
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing form first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

print(parent())

'''
- Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed. 

- Furthermore, the inner functions aren’t defined until the parent function is called. They’re locally scoped to parent(), meaning they only exist inside the parent() function as local variables. Try calling first_child(), this will thrown an error.

- Whenever you call parent(), the inner functions first_child() and second_child() are also called. But because of their local scope, they aren’t available outside of the parent() function.
'''

# Functions as Return Values:
print("\n\n------------ Functions as Return Values ------------")
'''
- Python allows us to return functions from functions. 
'''
def parent(num):
    def first_child():
        return "Hi, I am Netra kc"
    
    def second_child():
        return "Call me Yagya"
    
    if num == 1:
        return first_child
    else:
        return second_child
    
print(parent(2))

'''
- Note that we’re returning first_child without the parentheses. Recall that this means that we’re returning a reference to the function first_child. In contrast, first_child() with parentheses refers to the result of evaluating the function.
'''

first = parent(1)
second = parent(2)

'''
- The somewhat cryptic output means that the first variable refers to the local first_child() function inside of parent(), while second points to second_child().

- We can now use first and second as if they’re regular functions, even though you can’t directly access the functions they point to:

- We recognize the return values of the inner functions that you defined inside of parent().
'''