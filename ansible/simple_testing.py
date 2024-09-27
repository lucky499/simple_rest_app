# # Test on List objects
# my_list = [1,2,3,5]
# print(f"Original: {my_list}")

# temp_list = my_list.insert(1, 10)
# print(f"temp_list is: {temp_list}")

# pop_list = my_list.pop()
# print(f"pop_list is : {pop_list}")


def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Decorator 1
# Decorator 2
# Hello!
