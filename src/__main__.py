from src.app.console import Console
from termcolor import colored

console = Console()
console.new_game()
while True:
    console.draw_game()
    console.input()
    console.premakni_barabo()
    # princeska ujeta ali heroj ujet, konec igre
    if console.end_game() is True:
        break
    elif console.end_game() is False:

        console.level += 1
        console.rezultat += (console.maxKoraki - console.stetjeKorakov) * 2
        if console.level == 8:
            print(f'\033[33mČestitke, končali ste igro, princesa in heroj živit srečno skupaj vse do konca svojih dni!\033[0m')
            print(f'\033[92mVaš končni SCORE: {console.rezultat} in prišli ste do LEVEL: {console.level}\033[0m')
            break
        else:
            print('\033[32mPrinceska rešena...greš v naslednji nivo\033[0m')
            console.new_game()



