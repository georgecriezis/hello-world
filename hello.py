# this code greets the user by name
name = input("Enter your name: ").title()
clean = " ".join(name.split())
print(f"Hello, {clean}")