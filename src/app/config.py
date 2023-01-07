from enum import Enum


class GameConfig(Enum):
    INPUT_SPOROCILO_DX = 'input_sporocilo_dx'
    INPUT_SPOROCILO_DY = 'input_sporocilo_dy'
    INPUT_IZVEN_RAZPONE = 'input_izven_razpone'
    INPUT_NI_STEVILKA = 'input_ni_stevilka'
    SIMBOL_HEROJA = 'simbol_heroja'
    SIMBOL_PRINCESKE = 'simbol_princeske'
    SIMBOL_BARAB = 'simbol_barab'
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
    ODDALJENOST_BARABE = 1
    HITROST_HEROJA = 2
    MAX_KORAKI = 2
    KORAKI_SPODNJA_MEJA = 0
    REZULTAT = 0
    ST_BARAB = 2
    HITROST_BARABE = 2
    SIRINA_ZEMLJE = 13
    VISINA_ZEMLJE = 13
    KONCNI_LEVEL = 1
    INKREMENT_LEVEL = 1
    KORAKI_DEKREMENT = 1
    LEVEL_INICIALIZACIJA = 1

