# --------------------------
# | Dataman                |
# | M2HW1                  |
# | Drew Tadlock           |
# | 9/22/2024              |
# --------------------------

import games

def main():
    while True:
        try:
            print('1. Answer Checker')
            print('2. Memory Bank')
            print('3. Number Guesser')
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
