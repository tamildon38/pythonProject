number = 1
for row in range(1,4):
   for column in range(1,4):
      print(number , end =' ')
      number = number + 1
   print()

for number in range(1,11):
    if number == 5:
        continue
    else:
        print(number)

for number in range (1,11):
    if number == 15:
        break
    else:
        print(number)
else:
    print("all the numbers were printed")


def helloworld():
   print("hello world")
