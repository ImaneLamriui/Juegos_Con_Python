import random
import string
from Lang_FrameWork import Lang_FrameWk 

def select_lang_or_framework(name):
    name = random.choice(Lang_FrameWk)
    return(name).upper() 
# print(select_lang_or_framework(name))

language_selected_by_laptop = select_lang_or_framework(Lang_FrameWk)
      
letters_to_predict = set(language_selected_by_laptop)
letters_predicted = set()
# strings references: https://docs.python.org/3/library/string.html
letters_Alphabet = set(string.ascii_uppercase)
symbols = set(string.punctuation)

# print(f"letras_Abecedario :{letters_Alphabet}")
# print(f"Simbolos :{symbols}")

print("*******************************")
print("     ¡Bienvenido al juego!     ")
print("*******************************")

vidas = 5

while len(letters_to_predict) > 0 and vidas > 0:
    if vidas == 1:
      print(f"Te quedan {vidas} vida.Y has usado estas letras: {set(letters_predicted)}")
    elif vidas == 5:
      print(f"Te quedan {vidas} vida.")
    else:
      print(f"Te quedan {vidas} vidas.Y has usado estas letras: {set(letters_predicted)}")
    lenguaje = [letra if letra in letters_predicted else '-' for letra in language_selected_by_laptop]
    print(f"el lenguaje : {lenguaje}")

    letter_entered = input("escoge una letra: ").upper()
    if letter_entered in letters_Alphabet - letters_predicted or letter_entered in symbols - letters_predicted:
      letters_predicted.add(letter_entered)
      if letter_entered in letters_to_predict:
        letters_to_predict.remove(letter_entered)
        print("\n")
      else:
        vidas = vidas-1
       
        print("No has adivinado la letra intentalo otra vez.")
    elif letter_entered in letters_predicted:
      print("Esta letra ya ha sido introducida, intentalo con una nueva letra: ")
    else:
      print("ingresa una letra válida: ")

if vidas == 0:
    print(f"¡perdiste! vidas = {vidas} y la palabra era {language_selected_by_laptop}")

else:
    print(f"¡excelente! ¡adivinaste la palabra!: {language_selected_by_laptop}")
    

    
    
