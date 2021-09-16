from app.back.src.controllers.func.ctrl_func_getters import Ctrl_Func_Getters
from app.back.src.interfaces.i_repo import I_Repo


class Fact_Ctrl_Func:
    repo: I_Repo

    def __init__(self, repo: I_Repo):
        self.repo = repo

    def get_all_pkms(self):
        return Ctrl_Func_Getters(self.repo).get_all_pkms()

    def get_pkm_by_id(self, _id: int):
        return Ctrl_Func_Getters(self.repo).get_pkm_by_id(_id)

    def get_pkm_by_name(self, name: str):
        return Ctrl_Func_Getters(self.repo).get_pkm_by_name(name)
