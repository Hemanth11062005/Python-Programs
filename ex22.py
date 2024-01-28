#break continue pass
'''
break = used to terminate the loop entirely
continue - skips to the next iteration of the loop
pass = does noting acts as a placeholder
'''

while True:
    name = input("Enter your name:")
    if name!="":
        break
    
print(name,"\n")

phone_number = "123-456-789"
for i in phone_number:
    if i == "-":
        continue
    else:
        print(i,end=" ")

print("\n")
for i in range(1,21):
    if i == 13:
        pass
    print(i,end=" ")