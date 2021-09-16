from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.src.usecases.uc_getters import *
from app.back.tests.mocks.mocks import Mocks

repo = Repo_Txt()


class Test_UC_Getters:
    def test_get_all_pkms(self):
        exp_pkm_1 = Mocks.pkm_1()
        exp_pkm_2 = Mocks.pkm_2()
        exp_pkm_3 = Mocks.pkm_3()

        pkms = UC_Get_All_Pkms(repo)()

        assert len(pkms) == 151
        assert pkms[0].toDict() == exp_pkm_1.toDict()
        assert pkms[1].toDict() == exp_pkm_2.toDict()
        assert pkms[2].toDict() == exp_pkm_3.toDict()

    def test_get_pkm_by_id(self):
        exp_pkm = Mocks.pkm_1()

        act_pkm = UC_Get_Pkm_By_Id(repo)(1)

        assert act_pkm.toDict() == exp_pkm.toDict()

    def test_get_pkm_by_name(self):
        exp_pkm = Mocks.pkm_1()

        act_pkm = UC_Get_Pkm_By_Name(repo)('bulbasaur')

        assert act_pkm.toDict() == exp_pkm.toDict()
