# this code greets the user by name
name = input("Enter your name: ").title()
clean = " ".join(name.split())
print(f"Hello, {clean}")

# this code adds two numbers provided by the user

z = float(input("Enter a number for x: ")) + float(input("Enter a number for y: "))
print(z)