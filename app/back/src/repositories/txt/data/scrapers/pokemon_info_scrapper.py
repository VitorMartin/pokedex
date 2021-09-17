import requests

# noinspection PyInterpreter
base_url_all_pkms = 'https://pokeapi.co/api/v2/pokemon/'

if __name__ == '__main__':
    for i in range(1, 152):
        url = base_url_all_pkms + str(i)
        pkm = requests.get(url=url).json()
        pkm_id = pkm['id']
        pkm_name = pkm['name']

        with open('../pokemons/info/' + str(pkm_id) + '.txt', 'w') as file:
            # ID e nome
            write_str = (
                    'id:' + str(pkm_id) + '\n'
                                          'name:' + pkm_name + '\n'
            )

            # Tipos
            pkm_types = ''
            for _type in pkm['types']:
                pkm_types += _type['type']['name'] + ','
            pkm_types = pkm_types[:-1]
            write_str += 'types:' + pkm_types + '\n'

            # Sprite
            sprite_path = './pokedex/data/pokemons/sprites/' + str(pkm_id) + '.png'
            write_str += 'sprite:' + sprite_path

            file.write(write_str)
