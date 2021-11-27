from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.src.test_mcc_connection.blink import Blink


class Main_Back:
    def __init__(self, test_ctrl: bool = False, test_pico_connection: bool = False):
        print('Back iniciando...')
        
        if test_ctrl:
            self.repo = Repo_Txt()
            self.ctrl = Fact_Ctrl_Func(self.repo)
            print(self.ctrl.get_pkm_by_id(1))
            print(self.ctrl.get_pkm_by_name('ivysaur'))
            [print(pkm) for pkm in self.ctrl.get_all_pkms()[2:4]]

        elif test_pico_connection:
            self.ctrl = Blink()
            self.ctrl.blink()

        else:
            self.repo = Repo_Txt()
            self.ctrl = Fact_Ctrl_Func(self.repo)
