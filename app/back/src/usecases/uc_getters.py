from app.back.src.interfaces.i_repo import I_Repo


class UC_Get_All_Pkms:
    def __init__(self, repo: I_Repo):
        self.repo = repo

    def __call__(self):
        return self.repo.get_all_pkms()


class UC_Get_Pkm_By_Id:
    def __init__(self, repo: I_Repo):
        self.repo = repo

    def __call__(self, _id: int):
        return self.repo.get_pkm_by_id(_id)


class UC_Get_Pkm_By_Name:
    def __init__(self, repo: I_Repo):
        self.repo = repo

    def __call__(self, name: str):
        return self.repo.get_pkm_by_name(name)
