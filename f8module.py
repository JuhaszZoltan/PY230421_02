from random import randint

def random_karakter() -> str:
    code:int = randint(97, 122)
    return chr(code)


def random_jelszo(hossz:int) -> str:
    pwd:str = ''
    for _ in range(hossz):
        pwd += random_karakter()
    return pwd

# 65 - 90
# 97 - 122

