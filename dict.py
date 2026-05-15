d={}
d[100]="ashish"
d[200]="prashant"
d[300]="sandip"
print(d)
print(d.get(400,"Name")) #400 not available so Name will get printed

# rec={}
# n=int(input("Enter no of students: "))
# for i in range(n):
#     name=input("Enter your name: ")
#     per=float(input("Enter your %: "))
#     rec[name]=per
# print(rec)
# for x in rec:
#     print(x,"\t",rec[x])