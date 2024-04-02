#28278
#스택2
import sys
n=int(sys.stdin.readline().strip())
stack=[]

for _ in range(n):
  x=sys.stdin.readline().strip()
  if ' ' in x:
    x,y=map(int,x.split())
  else:
    x=int(x)
  if x==1:
    stack.append(y)
  elif x==2:
    if len(stack)==0:
      print(-1)
    else:
      a=stack.pop()
      print(a)
  elif x==3:
    print(len(stack))
  elif x==4:
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif x==5:
    if len(stack)==0:
      print(-1)
    else:
      b=stack[-1]
      print(b)