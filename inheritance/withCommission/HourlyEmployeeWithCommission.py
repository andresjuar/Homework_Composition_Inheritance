from dataclasses import dataclass
from HourlyEmployee import HourlyEmployee


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Empleado que se le paga en base a las horas trabajadas y que obtiene una comisión"""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed