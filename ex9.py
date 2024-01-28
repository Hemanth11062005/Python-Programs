import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python ex9.py <script> <first> <second> <third>")
    sys.exit(1)

# Unpack command-line arguments
script, first, second, third = sys.argv

# Rest of your code goes here
# ...
import sys
print(sys.argv)


print("The script is called:",script)
print("The first variable is:",first)
print("The second variable is:",second)
print("Your third variable is:",third)