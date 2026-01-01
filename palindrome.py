num=int(input("enter a number:"))
org=num
rev=0
for i in range(len(str(num))):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if org==rev:
    print(org,"palindrome number")
else:
    print(org,"not a palindrome number")
    