from abc import ABC, abstractmethod

from app.back.src.models.pkm import Pkm


class I_Repo(ABC):
    def get_all_pkms(self) -> list[Pkm]:
        pass

    @abstractmethod
    def get_pkm_by_name(self, name: str) -> Pkm:
        pass

    @abstractmethod
    def get_pkm_by_id(self, _id: int) -> Pkm:
        pass
