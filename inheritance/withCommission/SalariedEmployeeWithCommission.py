from dataclasses import dataclass
from SalariedEmployee import SalariedEmployee

@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Empleado que se le paga con un salario fijo mensual y que obtiene una comisión."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed