"""import math
def paint_calc(height,width,cover):
	num_cans =(height*width)/cover
	round_up_cans=math.ceil(num_cans)
	print(f"You will need {round_up_cans} cans of paint") #Ceil fonksiyonu ondalık sayıyı bi üst sayıya yuvarlar
test_h=int(input())
test_w=int(input())

coverage=5
paint_calc(height=test_h,width=test_w,cover=coverage)"""

"""def prime_checker(number):
	is_prime = True
	for i in range(2,number):
		if number %i== 0:
			is_prime=False
	if is_prime:
		print("It is a prime number")
	else:
		print("It is not a prime number")

n=int(input())
prime_checker(n)"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


"""def encrypt(plaint_text,shift_amount):
	cipher_text = ""
	for letter in plaint_text:
		position=alphabet.index(letter)
		new_position=position + shift_amount
		new_letter=alphabet[new_position]
		cipher_text += new_letter
	print("The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
	plain_text=""
	for letter in cipher_text:
		position =alphabet.index(letter)
		new_position=position-shift_amount
		plain_text+=alphabet[new_position]
	print(f"The decoded text is {plain_text}")

if direction =="encode":
	encrypt(plaint_text=text,shift_amount=shift)
else:
	encrypt(cipher_text=text,shift_amount=shift)

encrypt(plaint_text=text,shift_amount=shift)"""