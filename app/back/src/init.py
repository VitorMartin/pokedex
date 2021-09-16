from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.src.test_mcc_connection.blink import Blink


class Init:
    def __call__(self, test_pico_connection: bool = False):
        if test_pico_connection:
            return Blink()
        else:
            return Fact_Ctrl_Func(Repo_Txt())
