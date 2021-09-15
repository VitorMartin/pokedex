import os

from app.back.src.interfaces.i_repo import I_Repo
from app.back.src.models.pkm import Pkm


class Repo_Txt(I_Repo):
    path_to_data: str
    path_to_pkms: str
    path_to_sprites: str
    path_to_maps: str
    pkms: list[Pkm]
    id_to_name: dict[int, str]
    name_to_id: dict[str, int]

    def __init__(self):
        self.path_to_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        self.path_to_pkms = os.path.join(self.path_to_data, 'pokemons', 'info')
        self.path_to_sprites = os.path.join(self.path_to_data, 'pokemons', 'sprites')
        self.path_to_maps = os.path.join(self.path_to_data, 'pokemons')

        self.pkms = self.loadPkms()
        (self.id_to_name, self.name_to_id) = self.loadMaps()

    # ========== INTERNAL METHODS ========== #
    def loadPkms(self) -> list[Pkm]:
        _pkms: list[Pkm] = []
        for filename in os.listdir(self.path_to_pkms):
            _pkms.append(self.load_pkm_from_file(filename))
        return _pkms

    def loadMaps(self) -> (dict[int, str], dict[str, int]):  # retorna "DICT[ID] = NOME" e "DICT[NOME] = ID"
        _id_to_name: dict[int, str] = {}
        _name_to_id: dict[str, int] = {}

        for filename in os.listdir(self.path_to_pkms):
            pkm = self.load_pkm_from_file(filename)
            _id_to_name[pkm.id] = pkm.name
            _name_to_id[pkm.name] = pkm.id

        return _id_to_name, _name_to_id

    def load_pkm_from_file(self, filename: str) -> Pkm:
        with open(os.path.join(self.path_to_pkms, filename), 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
            _id = int(lines[0].split(':')[1])
            name = lines[1].split(':')[1]
            types = lines[2].split(':')[1].split(',')
            sprite_filename = lines[3].split(':')[1]
        return Pkm(_id, name, types, sprite_filename)

    # ========== EXTERNAL METHODS ========== #
    def get_pkm_by_id(self, _id: int):
        for pkm in self.pkms:
            if _id == pkm.id:
                return pkm
        return None

    def get_pkm_by_name(self, name: str):
        for pkm in self.pkms:
            if name == pkm.name:
                return pkm
        return None