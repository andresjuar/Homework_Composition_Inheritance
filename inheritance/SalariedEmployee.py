from dataclasses import dataclass
from Employee import Employee

@dataclass
class SalariedEmployee(Employee):
    """Empleado que se le paga con un salario fijo mensual"""

    monthly_salary: float
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage
