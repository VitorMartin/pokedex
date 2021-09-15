from app.back.src.usecases.uc_getters import *


class Ctrl_Func_Getters:
    repo: I_Repo

    def __init__(self, repo: I_Repo):
        self.repo = repo

    def get_pkm_by_id(self, _id: int) -> Pkm:
        return UC_Get_Pkm_By_Id(self.repo)(_id)

    def get_pkm_by_name(self, name: str) -> Pkm:
        return UC_Get_Pkm_By_Name(self.repo)(name)