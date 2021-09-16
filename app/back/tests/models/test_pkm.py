from app.back.src.models.pkm import Pkm
from app.back.tests.mocks.mocks import Mocks


class Test_Pkm:
    def test_regular_instance(self):
        exp_pkm = Mocks.pkm_dict_1()

        act_pkm = Mocks.pkm_1()

        assert isinstance(act_pkm, Pkm)
        assert act_pkm.toDict() == exp_pkm
