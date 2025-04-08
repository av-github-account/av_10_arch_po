# Определяем абстрактный базовый класс для всех конвертеров валют.

from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount: float) -> float:
        pass