from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.main_back import Main_Back


class Test_Main_Back:
    def test_main_back(self):
        main_back = Main_Back()

        assert isinstance(main_back, Main_Back)
        assert isinstance(main_back.ctrl, Fact_Ctrl_Func)
