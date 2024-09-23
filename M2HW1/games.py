import random
from numpy import clip
from typing import List, Tuple

def answer_checker():
    while True:
        try :
            problem = input('Enter a problem! Example: 1 + 1, or 11 * 25.35, or use \'0\' to exit: ')
            if problem == '0':
                break

            answer = eval(problem)
            user_answer = float(input('Great! Now, enter your answer: '))
            if user_answer == answer:
                print('Correct!')
                continue
            else:
                print(f'Incorrect! The answer was {answer}.')
        except Exception as err:
            print(err)
            continue    

def memory_bank():
    def random_problems(amount: int) -> List[Tuple[str, float]]:
        problems: List[Tuple[str, float]] = []

        for x in range(amount):
            operator = random.choice(['+', '-', '*', '/'])
            number1, number2 = 0, 0

            if operator in {'+', '-'}:
                number1 = round(random.uniform(1, 100), 2)
                number2 = round(random.uniform(1, 100), 2)

            elif operator in {'*', '/'}:
                number1 = random.randint(1, 100)
                number2 = random.randint(1, 100)

            equation = f'{number1} {operator} {number2}'
            answer = round(eval(equation), 2)
            
            problems.append((equation, answer))

        return problems

    problems = random_problems(10)
    print(problems)
    print('Implementation not yet done...')


def number_guesser():
    number = random.randint(9, 100)
    tries = 0
    print('Choose a random number between 9 and 100.')

    game_over = False
    while game_over == False:
        try:
            choice = int(input('Number: '))
            print(choice)
            tries += 1
            if (choice is number):
                print('You got it right!')
                game_over = True
            else:
                modifier = random.randint(1, 25)
                num1 = clip(number - modifier, 9, 100) 
                num2 = clip(number + modifier, 9, 100)
                print(f'The number is between {num1} and {num2}.')
                continue
            
        except KeyboardInterrupt:
            break

        except Exception as err:
            print(err)
            continue