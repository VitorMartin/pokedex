import requests

base_url_all_pkms = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%ID%.png'

if __name__ == '__main__':
    for i in range(667, 899):
        url = base_url_all_pkms.replace('%ID%', str(i))
        pkm_sprite = requests.get(url=url)
        open(f'../pokemons/sprites/{i}.png', 'wb').write(pkm_sprite.content)
