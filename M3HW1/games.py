import random
from numpy import clip

def answer_checker():
    while True:
        try:
            problem = input('Enter a problem! Example: 1 + 1, or 11 * 25.35: ')
            if problem == '0':
                break

            answer = eval(problem)
            user_answer = float(input('Great! Now, enter your answer: '))
            if user_answer == answer:
                print('Correct!')
                continue
            else:
                print(f'Incorrect! The answer was {answer}.')

        except KeyboardInterrupt:
            print('...\n')
            break


        except Exception as err:
            print(err)
            continue    

def memory_bank():
    problems = []
    while True:
        try:
            problem = input('Enter a problem to save: ')
            if (problem == '0'):
                break

            try:
                float(eval(problem))
                print(f'Added \'{problem}\'')
                problems.append(problem)

            except KeyboardInterrupt:
                continue

            except Exception as err:
                print(err)
                continue

        except KeyboardInterrupt:
            print('...\n')
            break

        except Exception as err:
            print(err)
            continue

    while problems.__len__() > 0:
        for problem in problems:
            try:
                answer = float(input('What is ' + f'\'{problem}\': '))
                if answer == eval(problem):
                    print('You got the answer right!')
                    problems.remove(problem)
                    continue
                else:
                    print('Wrong!')

            except KeyboardInterrupt:
                print('...\n')
                problems = []

            except Exception as err:
                print(err)
                continue

def number_guesser():
    number = random.randint(9, 100)
    tries = 0
    print('Choose a random number between 9 and 100.')

    while True:
        try:
            choice = int(input('Number: '))

            print(choice)
            tries += 1
            if (choice is number):
                print('You got it right!')
                break
            else:
                modifier = random.randint(1, 25)
                num1 = clip(number - modifier, 9, 100) 
                num2 = clip(number + modifier, 9, 100)
                print(f'The number is between {num1} and {num2}.')
                continue
            
        except KeyboardInterrupt:
            print('\n')
            break

        except Exception as err:
            print(err)
            continue