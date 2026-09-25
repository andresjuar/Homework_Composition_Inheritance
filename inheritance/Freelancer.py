from dataclasses import dataclass
from Employee import Employee

@dataclass
class Freelancer(Employee):
    """Freelancer que se le paga en base al número de horas trabajadas"""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked
