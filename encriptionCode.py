from random import randint
def otpGen():
	length = input('How long is your message? (number) ')
	name = input('What is the name of your otp? ')
	length = int(length)
	f = open(name, 'w+')
	i = 0
	while i < length:
		i += 1
		num = randint(1,26)
		num = str(num)
		f.write(num)
		f.write('\n')
def menu():
	a = 0
	while True:
		a = input('Generate one­time pad(1) \n Encrypt a message(2) \n Decrypt a message(3) \n Quit out of the program(4) ')
		if a == '1' or a == '2' or a == '3' or a == '4':
			break
	a = int(a)
	return a
def otpLoader():
	sheetName = input('What is the name of your otp? ')
	f = open(sheetName, 'r+')
	File = f.read()
	File = File.split()
	l = []
	for n in File:
		l.append(n)
	return (l)
def encryptionInput():
	i = input('What is your message? ')
	return i
def decryptionLoader():
	i = input('What file would you like to decrypt? ')
	f = open(i, 'r+')
	File = f.read()
	File = File.lower()
	l = []
	for n in File:
		l.append(n)
	return (l)
def fileGen(content):
	name = input('What will your file be called? ')
	f = open(name, 'w+')
	f.write(content)
def encryption(message, number):
	a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	encryptedMessage = []
	for n,l in enumerate(message):
		if l in a:
			encryptNum = number[n]
			alpNum = 0
			for aCycle in a:
				if l == aCycle:
					break
				alpNum += 1
			encryptNum = int(encryptNum)
			alpNum = alpNum + encryptNum
			if alpNum > 25:
				alpNum = alpNum - 26
			encryptedMessage.append(a[alpNum])
		else:
			encryptedMessage.append(l)
	final = ""
	for l in encryptedMessage:
		final = final + l
	return final
def decryption(message, number):
	a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	encryptedMessage = []
	for n,l in enumerate(message):
		if l in a:
			encryptNum = number[n]
			alpNum = 0
			for aCycle in a:
				if l == aCycle:
					break
				alpNum += 1
			encryptNum = int(encryptNum)
			alpNum = alpNum - encryptNum
			if alpNum < 0:
				alpNum = alpNum + 26
			encryptedMessage.append(a[alpNum])
		else:
			encryptedMessage.append(l)
	final = ""
	for l in encryptedMessage:
		final = final + l
	return final
while True:
	choice = menu()
	if choice == 1:
		otpGen()
	elif choice == 2:
		fileGen(encryption(encryptionInput(), otpLoader()))
	elif choice == 3:
		fileGen(decryption(decryptionLoader(), otpLoader()))
	else:
		break
