from app.back.src.main_back import Main_Back
from app.front.src.views.cli.splash_view import Splash_View
from app.front.src.views.cli.list_pkms_view import List_Pkms_View
from app.front.src.views.cli.clear_view import Clear_View
from app.front.src.models.button import Button
from app.front.src.models.display import Display


class Main_Front:
    def __init__(self):
        Clear_View()()
        Splash_View()()

        backend = Main_Back()

        display = Display()
        btn_select = Button(10)
        btn_back = Button(20)
        btn_up = Button(30)
        btn_down = Button(40)
        btn_left = Button(50)
        btn_right = Button(60)

        List_Pkms_View()(backend.ctrl.get_all_pkms())
