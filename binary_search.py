a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 10
# Expected output: 7 (since 8 is at index 7)
f=0
m=len(a)//2
l=len(a)
n=False
while n!=True:
    if a[m]==k:
        print(m)
        n=True
        break
    elif a[f]==k:
        print(f)
        n=True
        break
    elif a[l-1]==k:
        print(l-1)
        n=True
        break
    elif a[f]<k and a[m]>k:
        l=m
        m=(f+l)//2
    elif a[m]<k and a[l-1]>k:
        f=m
        m=(f+l)//2
    else:
        print("sorry not found")
        break