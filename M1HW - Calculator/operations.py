class Operations:
    ADDITION = (lambda firstNumber, secondNumber: firstNumber + secondNumber, 
    '+',
    '[green]Addition Chosen.[/green]')

    SUBTRACTION = (lambda firstNumber, secondNumber: firstNumber - secondNumber, 
    '-',
    '[yellow]Subtraction Chosen.[/yellow]')

    MULTIPLICATION = (lambda firstNumber, secondNumber: firstNumber * secondNumber, 
    '*',
    '[blue]Multiplication Chosen.[/blue]')

    DIVISION = (lambda firstNumber, secondNumber: firstNumber / secondNumber if secondNumber != 0 else float('inf'), 
    '/',
    '[purple]Division Chosen.[/purple]')

    EXPONENTIATION = (lambda firstNumber, secondNumber: firstNumber ** secondNumber, 
    '^',
    '[turquoise4]Exponentiation Chosen.[/turquoise4]')

    @staticmethod
    def get_operation(choice: str):
        if choice in {'1', 'add', '+'}:
            return Operations.ADDITION
        elif choice in {'2', 'sub', '-'}:
            return Operations.SUBTRACTION
        elif choice in {'3', 'mul', '*'}:
            return Operations.MULTIPLICATION
        elif choice in {'4', 'div', '/'}:
            return Operations.DIVISION
        elif choice in {'5', 'exp', '^'}:
            return Operations.EXPONENTIATION
        else:
            return None, '', '[red]Invalid Choice.[/red]'
