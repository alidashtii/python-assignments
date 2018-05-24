#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
import random
number = random.randint(1000,9999)
print ('Welcome to the Cows and Bulls Game!')
def compare(number , guess):
	cow_bull = [ 0, 0]
	for i in range(4):
		if guess[i] == number[i]:
			cow_bull[0] += 1
		elif guess[i] in number:
			cow_bull[1] += 1
	return cow_bull
	
playing = true
guesses = 0
while playing:
	guess = str(input('enter a number:'))
	cowNbull = compare ( number , guess)
	guesses += 1
	print ( 'you have' + cow_bull[0] + 'cows, and' + cow_bull[1]+ 'bulls')

	if cow_bull [0] == 4
		playing = false
		print (' you won')
	else:
		print ( ' try again')

		




