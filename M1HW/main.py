# --------------------------
# | Calculator Console App |
# | M1HW1_Tadlock          |
# | Drew Tadlock           |
# | 8/19/2024              |
# --------------------------

from operations import Operations
from rich import console as RichConsole, table as RichTable, panel as RichPanel # https://github.com/Textualize/rich
from typing import List, Optional
import os

console = RichConsole.Console()

def main(first_number: Optional[float] = None):
    while True:
        try:
            print_operations()
            
            choice = input('Enter an option: ').strip().lower()

            if choice in {'clear', '0'}:
                clear_console()
                return main()

            operation, sign, message = Operations.get_operation(choice)
            
            if not operation:
                console.print(message)
                continue
            
            console.print(message)
            nums = ask_for_numbers(first_number)
            clear_console()
            result = operation(nums[0], nums[1])

            print_results(nums, sign, result)

            first_number = result

        except KeyboardInterrupt:
            console.print('\n[red]Goodbye.[/red]')
            break

        except Exception as err:
            console.print(f'[red]{err}[/red]')

def print_operations():
    table = RichTable.Table(show_header=True, header_style='bold magenta')
    table.add_column('Option', style='dim')
    table.add_column('Operation')
    
    table.add_row('1.', 'Addition')
    table.add_row('2.', 'Subtraction')
    table.add_row('3.', 'Multiplication')
    table.add_row('4.', 'Division')
    table.add_row('5.', 'Exponent')
    table.add_row('0.', '[dim]Clear[/dim]')
    
    console.print(table)

def ask_for_numbers(first_number: Optional[float] = None) -> List[float]:
    def get_number(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt).strip())
            except ValueError:
                console.print('[red]Invalid input. Please enter a valid number.[/red]')

    if first_number is not None:
        return [first_number, get_number('Second Number: ')]
    else:
        return [get_number('First Number: '), get_number('Second Number: ')]

def print_results(nums: List[float], sign: str, result: float):
    text = f'[cyan]{nums[0]}[/cyan] [red]{sign}[/red] [cyan]{nums[1]}[/cyan] [red]=[/red] [bold green]{result}[/bold green]'
    console.print(RichPanel.Panel(text, title = '[bold]Result[/bold]', border_style = 'bold green', expand = False))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

main()