import sys
import os

# adding directory to python path
sys.path.append(os.getcwd())

from src.app.console import Console

console = Console()
console.new_game()

while True:
    console.draw_game()
    exit_terminal = console.input()
    match exit_terminal.value:
        case 'sys.exit()':
            sys.exit()
        case 'nadaljuj':
            # v primeru da so inputi validirani, ne morem uporabiti continue, ker mi štarta novo
            # iteracijo while loop-a, zato sem uporabil nested match case ¯\_(ツ)_/¯
            console.zemlja.premakni_barabo()
            result = console.end_game_conditions()
            match result.value:
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
                case 'nadaljuj':
                    continue



