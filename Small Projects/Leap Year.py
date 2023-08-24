year = int(input("enter a year: "))
hun = int((year // 100))
ten = int((year // 1000))
if hun % 2 == 0:
  print(str(year) + " was a leap year")
elif ten % 4 == 0:
  print(str(year) + " was a leap year")
else:
  print(str(year) + " not a leap year")