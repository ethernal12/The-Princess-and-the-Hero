import sys
import os

# adding directory to python path
sys.path.append(os.getcwd())

from src.app.console import Console

console = Console()
console.new_game()
while True:
    console.draw_game()
    console.input()
    console.premakni_barabo()
    zmaga = console.end_game_win()
    if console.end_game_loose():
        break
    elif zmaga == True:
        break
    elif zmaga == False:
        console.new_game()


