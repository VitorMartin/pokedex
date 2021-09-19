from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.src.test_mcc_connection.blink import Blink


class Init:
    def __call__(self, test_ctrl: bool = False, test_pico_connection: bool = False):
        if test_ctrl:
            ctrl = Fact_Ctrl_Func(Repo_Txt())
            print(ctrl.get_pkm_by_id(1))
            print(ctrl.get_pkm_by_name('ivysaur'))
            [print(pkm) for pkm in ctrl.get_all_pkms()[2:4]]
            return ctrl

        elif test_pico_connection:
            ctrl = Blink()
            ctrl.blink()
            return ctrl

        else:
            ctrl = Fact_Ctrl_Func(Repo_Txt())
            return ctrl
