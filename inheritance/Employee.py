from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Employee(ABC):
    """Representación de un empleado en una empresa."""

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Calcula cuanto el empleadodebe ser pagado."""