#program to print multiplicatin table of given number until 12 and util choice of continue is no
import time
while True:
    n = int(input("Enter which table:"))
    for i in range(1,13):
        print(i,"*",n,"=",i*n)
        time.sleep(1)
    ch = input("Do you want to continue: y/n")
    if(ch == "n" or ch == "N"):
        exit()