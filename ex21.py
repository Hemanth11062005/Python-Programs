#nested loops
'''
The inner loop will finish all of it's iterations before finishing one iteration of outer loop
'''

rows = int(input("How many rows:"))
columns = int(input("How many columns"))
symbol = input("Enter any symbol")

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print("\n")