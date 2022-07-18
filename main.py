import random
running = True
random_number = random.randint(0,100)
while running == True:
  guess = int(input("Guess the number "))
  if guess == random_number:
    print("U got it!!!!")
    running = False
  elif guess > random_number:
    print("To High")
  elif guess < random_number:
    print("to low")