from random import randint

def koszon(nev:str, napszak:str) -> None:
    print(f'Szia {nev}!')
    valasz:str = input(f'Hogy vagy ma {napszak}?: ')
    if 'jó' in valasz:
        print('örömmel hallom!')
    elif 'rossz' in valasz:
        print('sajnálattal hallom :(')
    else:
        print('rendben, értem...')
    print('akkor kezdjük!')


def feladat() -> bool:
    rsz = randint(1, 9)
    vlsz:str = int(input(f'mennyi {rsz} négyzete?: '))
    if vlsz == rsz**2:
        return True
    else:
        return False


def teszt(kerdesek_szama:int = 5) -> float:
    p:int = 0
    for ksz in range(kerdesek_szama):
        print(end=f'{ksz+1}.: ')
        if feladat():
            print('\tígy van')
            p += 1
        else: print('\tsajnos nem')
    return p / kerdesek_szama * 100