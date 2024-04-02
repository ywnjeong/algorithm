#2501
#약수 구하기
n,k=map(int, input().split())
i=1
while i<=n:
  if n%i==0:
    k-=1
    if k==0:
      print(i)
      break
  i+=1
if k>0:
  print(0)
