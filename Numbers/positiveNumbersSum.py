# Create a function that asks for positive numbers indefinitely. The program ends when a negative number is entered. Finally the program displays the sum of all the numbers entered

def numeros_positivos():
  Numbers = [0]
  
  
  for element in Numbers:
   
    number = int(input("insert a positive number: "))
    #if(number > 0):
    while number > 0:
      Numbers.append(number)
      nextNumber = element + number
      Sum = sum(Numbers)
      print(Numbers)
      print(nextNumber)
      number = int(input("insert a positive number: "))
    print("Final List!, the number is negative! : " + str(number))
    print("")
    break
  print("the sum of the numbers in the list is: " + str(Sum))
  
numeros_positivos()
