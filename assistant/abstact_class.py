from abc import ABC, abstractmethod


class BookInterface(ABC):
    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def show_one(self):
        pass

    @abstractmethod
    def show_page(self):
        pass