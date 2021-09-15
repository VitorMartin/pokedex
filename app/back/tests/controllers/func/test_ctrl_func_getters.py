from app.back.src.controllers.func.ctrl_func_getters import Ctrl_Func_Getters
from app.back.src.models.pkm import Pkm
from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.tests.mocks.mocks import Mocks

ctrl = Ctrl_Func_Getters(Repo_Txt())


class Test_Ctrl_Func_Getters:
    def test_get_pkm_by_id(self):
        exp_pkm = Mocks.pkm_1()

        act_pkm = ctrl.get_pkm_by_id(1)

        assert isinstance(act_pkm, Pkm)
        assert act_pkm.toDict() == exp_pkm.toDict()

    def test_get_pkm_by_name(self):
        exp_pkm = Mocks.pkm_1()

        act_pkm = ctrl.get_pkm_by_name('bulbasaur')

        assert isinstance(act_pkm, Pkm)
        assert act_pkm.toDict() == exp_pkm.toDict()
