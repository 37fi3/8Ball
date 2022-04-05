import random
import pyttsx3

response = [
    "it is certain", "it is decidely so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it yes", 
"Most likely", "outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", 
"Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
]

engine = pyttsx3.init("nsss")

greetings = [
    "That's a great question", "Thank's for asking", "Well"
]

name = input("Enter your name ")
question = input(name + ", what is your question for the magic 8 ball? ")

choice = random.randint (0,19)
greet_choice = random.randint(0,2)

engine.say(greetings[greet_choice] + str(name) + "The answer to your question, " + str(question) + "is    " + response[choice])
print("Magic 8 ball: ", response[choice])
engine.runAndWait()