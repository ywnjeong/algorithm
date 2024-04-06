def check(a,b):
  if a%b==0:
    print("multiple")
  elif b%a==0:
    print("factor")
  else:
    print("neither")
while True:
  a,b=map(int,input().split())
  if a==0 and b==0:
    break
  check(a,b)
