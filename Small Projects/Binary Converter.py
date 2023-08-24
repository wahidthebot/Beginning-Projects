num = int(input("enter a num: "))

list = []
while num > 0:
  if num % 2 == 0:
    list.append(0)
    num = num//2
  if num % 2 == 1:
    list.append(1)
    num = num//2
list.reverse()
print(list)