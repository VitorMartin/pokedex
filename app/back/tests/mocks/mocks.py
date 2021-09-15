from app.back.src.models.enums.en_pkm_key import PKM_KEY
from app.back.src.models.enums.en_pkm_type import PKM_TYPE
from app.back.src.models.pkm import Pkm


class Mocks:
    @staticmethod
    def pkm_1():
        return Pkm(
            1, 'bulbasaur', [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value], './pokedex/data/pokemons/sprites/1.png'
        )

    @staticmethod
    def pkm_2():
        return Pkm(
            2, 'ivysaur', [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value], './pokedex/data/pokemons/sprites/2.png'
        )

    @staticmethod
    def pkm_3():
        return Pkm(
            3, 'venusaur', [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value], './pokedex/data/pokemons/sprites/3.png'
        )

    @staticmethod
    def pkm_dict_1():
        return {
            PKM_KEY.ID.value: 1,
            PKM_KEY.NAME.value: 'bulbasaur',
            PKM_KEY.TYPES.value: [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value],
            PKM_KEY.SPRITE_FILENAME.value: './pokedex/data/pokemons/sprites/1.png'
        }

    @staticmethod
    def pkm_dict_2():
        return {
            PKM_KEY.ID.value: 2,
            PKM_KEY.NAME.value: 'ivysaur',
            PKM_KEY.TYPES.value: [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value],
            PKM_KEY.SPRITE_FILENAME.value: './pokedex/data/pokemons/sprites/2.png'
        }

    @staticmethod
    def pkm_dict_3():
        return {
            PKM_KEY.ID.value: 3,
            PKM_KEY.NAME.value: 'venusaur',
            PKM_KEY.TYPES.value: [PKM_TYPE.GRASS.value, PKM_TYPE.POISON.value],
            PKM_KEY.SPRITE_FILENAME.value: './pokedex/data/pokemons/sprites/3.png'
        }
