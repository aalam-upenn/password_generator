#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#choosing random items from the list defined above to form the password

password_letters = random.sample(letters, nr_letters)
password_numbers = random.sample(numbers, nr_numbers)
password_symbols = random.sample(symbols, nr_symbols)

#combining letters, numbers and symbols
final_list = password_letters + password_numbers + password_symbols

#shuffling letters, numbers and symbols to form the password so that they are not in a serial of letters first, then numbers, then symbols

random.shuffle(final_list)

#converting list to string to print the password_letters
password = ''.join(final_list)
print("Here is your password: "+ password)