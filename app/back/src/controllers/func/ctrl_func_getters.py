from typing import List

from app.back.src.models.pkm import Pkm
from app.back.src.usecases.uc_getters import *


class Ctrl_Func_Getters:
    def __init__(self, repo: I_Repo):
        self.repo = repo

    def get_all_pkms(self) -> List[Pkm]:
        return UC_Get_All_Pkms(self.repo)()

    def get_pkm_by_name(self, name: str) -> Pkm:
        return UC_Get_Pkm_By_Name(self.repo)(name)

    def get_pkm_by_id(self, _id: int) -> Pkm:
        return UC_Get_Pkm_By_Id(self.repo)(_id)
