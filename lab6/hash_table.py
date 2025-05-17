from typing import Dict
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def create_hash_table(size) -> Dict:
    return {
        'size' : size,
        'table' : [None] * size,
        'count' : 0
    }


def find_key(word: str) -> int:
    word = word.lower()
    first_letter = alphabet.find(word[0])
    second_letter = alphabet.find(word[1])
    key = first_letter * 33 + second_letter
    return key

def hash1(key: int, hs: Dict) -> int:
    return key % hs['size']

def hash2(key: int, hs: Dict) -> int:
    return 1 + (key % (hs['size'] - 1))

def insert(hs: Dict, word:str, value:str) -> None:
    key = find_key(word)
    index = hash1(key, hs)
    if hs['table'][index] is None:
        hs['table'][index] = {word:value}
        hs['count'] += 1
    else:
        i = 0
        while hs['table'][index] is not None:
            index = (hash1(key, hs) + i * hash2(key, hs)) % hs['size']
            i += 1
        hs['table'][index] = {word:value}
        hs['count'] += 1
        

def find(hs: Dict, word:str) -> str:
    key = find_key(word)
    index = hash1(key, hs)
    if hs['table'][index] is None:
        raise KeyError(f"Слово '{word}' не найдено")
    if next(iter(hs['table'][index])) == word: 
        return hs['table'][index][word]
    else:
        i = 0
        while next(iter(hs['table'][index])) != word:
            index = (hash1(key) + i * hash2(key)) % hs['size']
            i += 1
        return hs['table'][index][word]
    
def deleting(hs: Dict, word:str) -> None:
    key = find_key(word)
    index = hash1(key, hs)
    
    if hs['table'][index] is None:
        return
    if next(iter(hs['table'][index])) == word:
        hs['table'][index] = None
        hs['count'] -= 1
        return
    else:
        i = 0
        while True:
            index = (hash1(key, hs) + i * hash2(key, hs)) % hs['size']
            if hs['table'][index] is None:
                return
            if next(iter(hs['table'][index])) == word:
                hs['table'][index] = None
                hs['count'] -= 1
                return
            i += 1
    

def update_hash_table(hs: Dict):
    new_size = hs['size'] + 10
    new_table = create_hash_table(new_size)
    for item in hs['table']:
        if item is not None:
            for key, value in item.items():
                insert(new_table, key, value)
    return new_table


# hs = create_hash_table(10)

# print(hs)

# insert(hs,'ыаваы','5')
# insert(hs,'ыыфвыв','4')
# insert(hs,'вввв','4')

# insert(hs,'крк','3')
# insert(hs,'ыреккы','1')
# print(hs)
# insert(hs,'ырекраы','2')
# insert(hs,'крк','1212222222')
# insert(hs,'ыреккы','121222')
# print(hs)
# insert(hs,'чч','1212')
# insert(hs,'ффеккы','121212')


# x = find('ыреккы')
# print("xxxx", x)
# print(hs)
# # delteing('вввв')
# # hs = update_hash_table()
# print(hs)

