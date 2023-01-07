from colored import fg, attr


def messages(instance, game_condition):
    konec_igre = f'{fg("light_green")}Vaš končni SCORE: {instance.rezultat} in prišli ste do LEVEL: {instance.level}{attr(0)}'
    match game_condition.value:
        case 'zmaga_končaj_igro':
            print(
                f'{fg("gold_1")}Čestitke, končali ste igro, princesa in heroj živita srečno skupaj vse do konca svojih dni!{attr(0)} ')
            print(konec_igre)
        case 'naslednji_nivo':
            print(f'{fg("light_green")}Princeska rešena...greš v naslednji nivo')
        case 'princeska_ujeta':
            print(f'{fg("red_1")}Baraba ujela princesko!Konec igre... {attr(0)}')
            print(konec_igre)
        case 'heroj_ujet':
            print(f'{fg("red_1")}Heroj ujet! Število življenj = {instance.zemlja.hero.st_ostalih_zivljenj()}{attr(0)}')
        case 'poraz_končaj_igro':
            print(f'{fg("red_1")}Konec igre... {attr(0)}')
            print(konec_igre)
        case 'koraki_preseženi':
            print(f'{fg("red_1")}Presegli ste določeno število potez, igre konec! {attr(0)}')
            print(konec_igre)
        case 'podatki_igre':
            print(f'{instance.zemlja.hero.st_ostalih_zivljenj()}')
            print(f'{fg("gold_1")}{instance.level} LEVEL{attr(0)}')
            print(f'{fg("gold_1")}SCORE {instance.rezultat}{attr(0)}')
            print('---------')
            print(f'{fg("gold_1")}Preostali koraki {instance.maxKoraki}{attr(0)}')
            print('-------------------')
        case 'simbol_barab':
            print(fg('red_1') + 'B ' + attr('reset'), end='')
        case 'simbol_heroja':
            print(fg('light_green') + 'H ' + attr('reset'), end='')
        case 'simbol_princeske':
            print('\u2640 ', end='')
        case 'input_izven_razpone':
            print(fg('red_1') + 'Vnesli se številko izven razpona, ponovno vnesite številko dx.' + attr('reset'))
        case 'input_ni_stevilka':
            print(fg('red_1') + 'Prosim vnesite številko dx med +2 in -2' + attr('reset'))
        case 'narisi_piko':
            print('. ', end='')
        case 'input_sporocilo_dx':
            return input(fg('light_green') + 'Vnesi dx med +2 in -2:' + attr('reset'))
        case 'input_sporocilo_dy':
            return input(fg('light_green') + 'Vnesi dy med +2 in -2:' + attr('reset'))

