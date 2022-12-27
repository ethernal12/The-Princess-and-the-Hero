from src.app.console import Console

console = Console()
console.new_game()

while True:
    console.draw_game()
    console.input()
    console.premakni_barabo()
    if console.end_game():
        break



