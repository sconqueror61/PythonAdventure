# Morse kodu tablosu
MORSE_CODE_DICT = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
 ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
'(': '-.--.', ')': '-.--.-', ' ': '/'
}

def encrypt(message):
	cipher = ''
	for letter in message.upper():
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += '/ '
	return cipher.strip()

def decrypt(message):
	message += ' '
	decipher = ''
	citext = ''
	for letter in message:
		if letter != ' ':
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2:
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
				citext = ''
	return decipher

def main():
	choice = input("1: Encrypt\n2: Decrypt\nEnter your choice: ")

	if choice == '1':
		message = input("Enter message to encrypt: ")
		result = encrypt(message)
	elif choice == '2':
		message = input("Enter message to decrypt: ")
		result = decrypt(message)
	else:
		result = "Invalid choice. Please enter 1 or 2."

	print(f"Result: {result}")

if __name__ == "__main__":
	main()
