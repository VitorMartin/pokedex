from app.back.src.factories.controllers.func.fact_ctrl_func import Fact_Ctrl_Func
from app.back.src.init import Init


class Test_init:
    def test_init(self):
        ctrl = Init()()

        assert isinstance(ctrl, Fact_Ctrl_Func)
