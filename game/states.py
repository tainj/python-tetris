from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_events(self, event):
        """Метод для обработки событий. Должен быть реализован в дочерних классах."""
        pass

    @abstractmethod
    def update(self):
        """Метод для обновления. Должен быть реализован в дочерних классах."""
        pass

    @abstractmethod
    def render(self):
        """Метод для отрисовки кадра. Должен быть реализован в дочерних классах."""
        pass