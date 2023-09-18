# Coded only one property for demo purposes – classes usually have several properties
class Employee:
    def __init__(self, id, name, salary):
        self._id = id
        self._name = name        
        self.salary = salary
        
    # Decorators that define PROPERTIES
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_sal):
        #BUSINESS RULE: salary between 30K and 200K
        if 30_000 <= new_sal <= 200_000:
            self._salary = new_sal
        else:
            raise ValueError(f"New value of salary, {new_sal}, outside allowable range")
        
an_employee = Employee(123, "Pete Moss", 2_135_234.56)
# Where's the Value error?
print(f'Employee Salary: {an_employee.salary}')