def greet_user(name):
    return f"Hello, {name}! Welcome to Python 🚀"

if _name_ == "_main_":
    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)