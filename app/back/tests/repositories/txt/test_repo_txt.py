from app.back.src.repositories.txt.repo_txt import Repo_Txt
from app.back.tests.mocks.mocks import Mocks


class Test_Repo_Txt:
    def test_init(self):
        repo = Repo_Txt()

        exp_pkm_1 = Mocks.pkm_1()
        exp_pkm_2 = Mocks.pkm_2()
        exp_pkm_3 = Mocks.pkm_3()

        assert repo.pkms[0].toDict() == exp_pkm_1.toDict()
        assert repo.pkms[1].toDict() == exp_pkm_2.toDict()
        assert repo.pkms[2].toDict() == exp_pkm_3.toDict()
        assert repo.id_to_name[1] == 'bulbasaur'
        assert repo.id_to_name[2] == 'ivysaur'
        assert repo.id_to_name[3] == 'venusaur'
        assert repo.name_to_id['bulbasaur'] == 1
        assert repo.name_to_id['ivysaur'] == 2
        assert repo.name_to_id['venusaur'] == 3
