n=int(input("Enter no of courses:"))
if n<1:
    print("Invalid")
    exit(0)
res=[]
for i in range(n):
    print("Enter name and marks:")
    sub=input()
    mark=int(input())
    if mark<0 or mark>100:
        print("Invalid mark")
        exit(0)
    if mark>=80:
        res.append((sub,mark))
if res:
    print("The courses cleared are:")
    for x,y in res:
        print(f"{x} {y}")