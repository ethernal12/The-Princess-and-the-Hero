from src.app.console import Console

console = Console()
console.new_game()
while True:
    console.draw_game()
    console.input()
    console.premakni_barabo()
    # princeska ujeta ali heroj ujet, konec igre
    if console.end_game() is True:
        break
    # princeska rešena, igralec gre v naslednji nivo
    elif console.end_game() is False:
        print('\033[32mPrinceska rešena in pade v objem pogumnemu heroju...\033[0m')
        console.level += 1
        console.rezultat += (console.max_koraki - console.stetjeKorakov) * 2
        console.new_game()



