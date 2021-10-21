from copy import copy
from typing import List

from app.front.src.models.enums.en_pkm_key import PKM_KEY


class Pkm:
    def __init__(self, _id: int, name: str, types: List[str], sprite_filename: str):
        self.id = _id
        self.name = name
        self.types = copy(types)  # copiar lista para evitar memory leak
        self.sprite_filename = sprite_filename

    def __str__(self):
        ret = (
            '{\n' +
            '\t"' + PKM_KEY.ID.value + '": ' + str(self.id) + ',\n' +
            '\t"' + PKM_KEY.NAME.value + '": "' + self.name + '",\n' +
            '\t"' + PKM_KEY.TYPES.value + '": ['
        )
        for _type in self.types:
            ret += _type + ', '
        ret = ret[:-2]
        ret += '], \n'
        ret += '\t"' + PKM_KEY.SPRITE_FILENAME.value + '": "' + self.sprite_filename + '"\n}'

        return ret

    @staticmethod
    def fromDict(d: dict):
        return Pkm(
            int(d[PKM_KEY.ID.value]),
            str(d[PKM_KEY.NAME.value]),
            d[PKM_KEY.TYPES.value],
            str(d[PKM_KEY.SPRITE_FILENAME.value])
        )

    def toDict(self):
        return {
            PKM_KEY.ID.value: self.id,
            PKM_KEY.NAME.value: self.name,
            PKM_KEY.TYPES.value: self.types,
            PKM_KEY.SPRITE_FILENAME.value: self.sprite_filename
        }
