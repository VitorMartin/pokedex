import requests

base_url_all_pkms = 'https://pokeapi.co/api/v2/pokemon/'

if __name__ == '__main__':
    for i in range(1, 152):
        url = base_url_all_pkms + str(i)
        pkm = requests.get(url=url).json()
        pkm_id = pkm['id']
        pkm_name = pkm['name']

        with open(f'../pokemons/{pkm_id}.txt', 'w') as file:
            # ID e nome
            write_str = (
                f'id:{pkm_id}\n'
                f'name:{pkm_name}\n'
            )

            # Tipos
            pkm_types = ''
            for type in pkm['types']:
                pkm_types += type['type']['name'] + ','
            pkm_types = pkm_types[:-1]
            write_str += f'types:{pkm_types}\n'

            # Sprite
            sprite_url = pkm['sprites']['front_default']
            write_str += f'sprite:{sprite_url}'

            file.write(write_str)