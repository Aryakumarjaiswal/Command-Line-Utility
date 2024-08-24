import argparse

# Step 1: Create parser
parser = argparse.ArgumentParser(description="A simple calculator utility")

# Step 2: Define positional arguments
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")

# Step 3: Parse arguments
args = parser.parse_args()

# Step 4: Implement logic
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    result = args.num1 / args.num2

print(f"The result is: {result}")

#In terminal:cd "path_of_directory_containing_file"
#python filename.py 2 3 multiply
