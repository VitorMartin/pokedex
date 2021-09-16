from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.main import main


class Test_Main:
    def test_main(self):
        ctrl = main()

        assert isinstance(ctrl, Fact_Ctrl_Func)
