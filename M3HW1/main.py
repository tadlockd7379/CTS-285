# --------------------------
# | Dataman                |
# | M3HW1                  |
# | Drew Tadlock           |
# | 10/6/2024              |
# --------------------------

import games

def main():
    while True:
        try:
            print('----------------------')
            print('1. Answer Checker')
            print('2. Memory Bank')
            print('3. Number Guesser')
            print('----------------------')
            choice = input('Choose an option: ').strip().lower()

            if (choice in {'1', 'answer', 'answer checker'}):
                games.answer_checker()
            elif (choice in {'2', 'memory', 'memory bank'}):
                games.memory_bank()
            elif (choice in {'3', 'number', 'number guesser'}):
                games.number_guesser()
            else: 
                continue
        
        except KeyboardInterrupt:
            print('\nGoodbye.')
            break

        except Exception as err:
            print(err)  

main()
