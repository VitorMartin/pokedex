from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.repositories.txt.repo_txt import Repo_Txt


class Init:
    def __call__(self):
        return Fact_Ctrl_Func(Repo_Txt())
