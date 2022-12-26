from src.app.console import Console
from src.domain.baraba import Baraba



console = Console()
console.new_game()

while True:
    console.draw_game()
    console.input()
    console.end_game()

