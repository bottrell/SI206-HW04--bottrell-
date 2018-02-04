import random

def user_input():
	question = input("What is your question?")
	return question

def pick_answer():
	answers=["It is certain", "It is decidedly so", "Without a doubt","Yes definitely", "You may rely on it", "As I see it, yes", "Most likely","Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later","Better not tell you now", "Cannot predict now", "Concentrate and ask again","Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

	picked=random.choice(answers)

	return picked

question = user_input()
while (question != "quit"):
	print (pick_answer())
	if ((question[-1]) != '?'):
		print ("I'm sorry, I can only answer questions.")
	question = user_input()

