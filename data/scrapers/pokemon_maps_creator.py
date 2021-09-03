import os

dir = r'../pokemons/info/'

if __name__ == '__main__':
    # KEY: name ==> VAL: ID
    with open('../pokemons/name_to_id.txt', 'w') as file_map:
        pkm_pairs = {}

        for entry in os.scandir(dir):
            if (
                entry.is_file()
                and entry.path.endswith('.txt')
            ):
                with open(entry.path) as file_pkm:
                    for line in file_pkm:
                        if line.startswith('id'):
                            pkm_id = line.split(':')[1]
                            pkm_id = pkm_id[:-1]
                        elif line.startswith('name'):
                            pkm_name = line.split(':')[1]
                            pkm_name = pkm_name[:-1]
                    pkm_pairs[pkm_name] = pkm_id
        
        write_str = ''
        for (key, val) in sorted(pkm_pairs.items()):
            write_str += f'{key}:{val}\n'
        write_str = write_str[:-1]
        file_map.write(write_str)

    # KEY: ID ==> VAL : name
    with open('../pokemons/id_to_name.txt', 'w') as file_map:
        pkm_pairs = {}

        for entry in os.scandir(dir):
            if (
                entry.is_file()
                and entry.path.endswith('.txt')
            ):
                with open(entry.path) as file_pkm:
                    for line in file_pkm:
                        if line.startswith('id'):
                            pkm_id = line.split(':')[1]
                            pkm_id = pkm_id[:-1]
                        elif line.startswith('name'):
                            pkm_name = line.split(':')[1]
                            pkm_name = pkm_name[:-1]
                    pkm_pairs[int(pkm_id)] = pkm_name
        
        write_str = ''
        for (key, val) in sorted(pkm_pairs.items()):
            write_str += f'{key}:{val}\n'
        write_str = write_str[:-1]
        file_map.write(write_str)
