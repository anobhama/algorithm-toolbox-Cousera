import  sys

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

x=int(input())
y=int(input())
gcd = compute_gcd(x,y)
print(gcd)