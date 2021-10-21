from typing import List
from app.back.src.main_back import Main_Back
from app.front.src.models.pkm import Pkm

class List_Pkms_View:
    def __init__(self):
        pass

    def __call__(self, list_pkms: List[Pkm]):
        for pkm in list_pkms:
            print(f"{pkm.id} - {pkm.name}")
