"""import random 
random_side = random.randint(0,1)
if random_side==1:
	print("Yazı")
if random_side==0:
	print("Tura")"""

"""Turkıye = ["Adana25","Bursa	238","İstanbul	25","İzmir	9","Trabzon	36"]

print(Turkıye[-1])
Turkıye.append("Bursa")
print(Turkıye) """

"""names= names_string.split(", ")
import random

num_items=len(names)
random_choice = random.randint(0, num_items-1)
person_who_will_pay = names [random_choice]
print(person_who_will_pay + "This number will pay!!!")"""

"""fruits = ["Çİlek", "Nectar", "Elma", "Üzüm","Ayva", "Çeri","Armıt"]
vegetables= ["Ispanak"," Karnıobahar"," Kereviz", "pAtates"]

dirty_dozen=[fruits,vegetables]

print(dirty_dozen)"""

"""line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]

map=[line1,line2,line3]
print("Hiding your treasure! X marks the Spot")
position=input()
letter= position[0].lower()#Kullanıcının gireceği ilk değer(sütun)
abc=["a","b","c"]
letter_index=abc.index(letter)
number_index= int(position[1])-1
map[number_index][letter_index]="X"

print(f"{line1}\n{line2}\n{line3}\n")"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")


