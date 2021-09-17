import requests

base_url_all_pkms = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%ID%.png'

if __name__ == '__main__':
    for i in range(1, 152):
        url = base_url_all_pkms.replace('%ID%', str(i))
        pkm_sprite = requests.get(url=url)
        with open('../pokemons/sprites/' + str(i) + '.png', 'wb') as file:
            file.write(pkm_sprite.content)
