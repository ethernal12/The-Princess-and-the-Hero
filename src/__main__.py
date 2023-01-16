import sys
import os
from app.config import GameConfig

# adding directory to python path!
sys.path.append(os.getcwd())

from src.app.console import Console

app = Console()
app.new_game()

while True:
    app.draw_game()
    exit_terminal = app.input()
    match exit_terminal.value:
        case GameConfig.EXIT_GAME_COMMAND.value:
            sys.exit()
        case GameConfig.NADALJUJ_ZANKO.value:
            # v primeru da so inputi validirani, ne morem uporabiti continue, ker mi štarta novo
            # iteracijo while loop-a, zato sem uporabil nested match case ¯\_(ツ)_/¯
            app.zemlja.premakni_barabo()
            result = app.end_game_conditions()
            match result.value:
                case GameConfig.HEROJ_UJET.value:
                    break
                case GameConfig.PRINCESA_UJETA.value:
                    break
                case GameConfig.ZMAGA.value:
                    break
                case GameConfig.KORAKI_PRESEZENI.value:
                    break
                case GameConfig.NASLEDNJI_NIVO.value:
                    app.new_game()
                case GameConfig.NADALJUJ_ZANKO.value:
                    continue
