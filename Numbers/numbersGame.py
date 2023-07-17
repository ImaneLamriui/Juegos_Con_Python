#Create a function that asks for numbers infinitely. The numbers entered must be greater than the previous one,  The program will end when a number less than the previous one is entered

def Juego_numeros():

  Numbers = [0]
  element = 0
  number = int(input("insert a bigger number: "))
  Numbers.append(number)
 
  while Numbers[element] < Numbers[element+1]:
    number = int(input("insert a greater number: "))
    Numbers.append(number)
    print(Numbers)
    element+=1
  print("")
  print("Final List!, the number isn't greater than the previous one! : " + str(Numbers))
Juego_numeros()