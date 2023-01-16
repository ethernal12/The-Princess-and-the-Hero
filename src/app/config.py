from enum import Enum


class GameConfig(Enum):
    INPUT_SPOROCILO_DX = 'input_sporocilo_dx'
    INPUT_SPOROCILO_DY = 'input_sporocilo_dy'
    ERROR_INPUT_IZVEN_RAZPONE = 'input_izven_razpone'
    ERROR_INPUT_NI_STEVILKA = 'input_ni_stevilka'
    PRINT_HEROJA = 'heroja'
    PRINT_PRINCESKE = 'princeska'
    PRINT_BARABO = 'barabe'
    SIMBOL_PRINCESKE = '\u2640 '
    PODATKI_IGRE = 'podatki_igre'
    HEROJ_UJET = "heroj_ujet"
    PRINCESA_UJETA = "princeska_ujeta"
    KORAKI_PRESEZENI = "koraki_preseženi"
    ZMAGA = "zmaga_končaj_igro"
    PORAZ = "poraz_končaj_igro"
    NASLEDNJI_NIVO = "naslednji_nivo"
    NADALJUJ_ZANKO = 'nadaljuj'
    EXIT_GAME_INPUT = 'q'
    EXIT_GAME_COMMAND = 'sys.exit()'
    NARISI_PIKO = 'narisi_piko'
    BORDER_COLOR = 'light_cyan'
    ODDALJENOST_BARABE = 1
    HITROST_HEROJA = 2
    MAX_KORAKI = 100
    KORAKI_SPODNJA_MEJA = 0
    REZULTAT = 0
    ST_BARAB = 5
    HITROST_BARABE = 2
    SIRINA_ZEMLJE = 13
    VISINA_ZEMLJE = 13
    KONCNI_LEVEL = 5
    INKREMENT_LEVEL = 1
    KORAKI_DEKREMENT = 1
    LEVEL_INICIALIZACIJA = 1
    BORDER_TOP_BOTTOM = 'border_top_bottom'
    BORDER_LEFT = 'border_left'
    BORDER_RIGHT = 'border_right'
    PREMIK_DESNO = 'D'
    PREMIK_LEVO = 'A'
    PREMIK_GOR = 'W'
    PREMIK_DOL = 'S'

