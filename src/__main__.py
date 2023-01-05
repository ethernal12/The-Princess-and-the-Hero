
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
    console.zemlja.premakni_barabo()
    result = console.end_game_conditions()
    match result:
        case 'heroj_ujet':
            break
        case 'princeska_ujeta':
            break
        case 'zmaga_končaj_igro':
            break
        case 'koraki_preseženi':
            break
        case 'naslednji_nivo':
            console.new_game()


