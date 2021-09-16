from copy import copy

from app.back.src.models.enums.en_pkm_key import PKM_KEY


class Pkm:
    id: int
    name: str
    types: list[str]
    sprite_filename: str  # caminho do arquivo

    def __init__(self, _id: int, name: str, types: list[str], sprite_filename: str):
        self.id = _id
        self.name = name
        self.types = copy(types)  # copiar lista para evitar memory leak
        self.sprite_filename = sprite_filename

    def __str__(self):
        return (
            f'{{\n'
            f'\t"{PKM_KEY.ID.value}": {self.id},\n'
            f'\t"{PKM_KEY.NAME.value}": "{self.name}",\n'
            f'\t"{PKM_KEY.TYPES.value}": {self.types},\n'
            f'\t"{PKM_KEY.SPRITE_FILENAME.value}": "{self.sprite_filename}"\n'
            f'}}'
        )

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
