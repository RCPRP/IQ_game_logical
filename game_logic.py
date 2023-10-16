import random
computer_choice=random.randint(1,10)
attempts = 0
while attempts<3:
    user_choice = int(input('Guess the number: '))
    if user_choice==computer_choice:
        print('correct guess')
        break
    elif user_choice>computer_choice:
        print('too high')
    else:
        print('too low')
    attempts+=1
if attempts>=3:
    print('Failed 3 times')
print('GAME OVER')
