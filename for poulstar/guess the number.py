import random
answer = random.randint(0, 1000)

guess = input('Guess the number: ')
guess = int(guess)

for i in range(1000):
    if guess > answer:
        guess = input('It is smaller than that: ')
        guess = int(guess)
    elif guess < answer:
        guess = input('It is bigger than that: ')
        guess = int(guess)
    else:
        print('Yey. You found the answer.', answer)
        exit()
    