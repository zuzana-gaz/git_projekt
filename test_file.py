from functools import reduce

class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float, hourly_rate: float):
        self.__emp_id = emp_id
        self.name = name
        self.__base_salary = base_salary
        self.hourly_rate = hourly_rate

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def base_salary(self):
        return self.__base_salary

    def __str__(self):
        return f"ID: {self.emp_id} | Zamestnanec: {self.name} | Základ: {self.base_salary} €"