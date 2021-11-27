from app.front.src.main_front import Main_Front


class Test_Main_Front:
    def test_main_front(self):
        main_front = Main_Front()

        assert isinstance(main_front, Main_Front)
