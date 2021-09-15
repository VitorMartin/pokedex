from app.back.src.interfaces.i_repo import I_Repo
from app.back.src.models.pkm import Pkm


class UC_Get_Pkm_By_Id:
    repo: I_Repo

    def __init__(self, repo: I_Repo):
        self.repo = repo

    def __call__(self, _id: int) -> Pkm:
        return self.repo.get_pkm_by_id(_id)


class UC_Get_Pkm_By_Name:
    repo: I_Repo

    def __init__(self, repo: I_Repo):
        self.repo = repo

    def __call__(self, name: str) -> Pkm:
        return self.repo.get_pkm_by_name(name)
