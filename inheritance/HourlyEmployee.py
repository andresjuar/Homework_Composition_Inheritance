from dataclasses import dataclass
from Employee import Employee


@dataclass
class HourlyEmployee(Employee):
    """Empleado que se le paga en base a las horas trabajadas"""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost
