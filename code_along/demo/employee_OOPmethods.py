'''
Code a class that models employees that:
● Has 4 fields: empID, empName, empDept, empSalary
● All fields initialized in CTOR
● empSalary must be between 30K and 200K
● If outside this range, a diagnostic is printed
● Values outside this range force empSalary to None
● This class has two methods:
● print_me, which prints the values of all the fields
● give_emp_pct_raise, which takes an arg representing a percent
raise for the employee
● The arg must be between 10 and 20
● If outside this range, a diagnostic is printed
● If after the raise calculation the salary exceeds 200K, the salary
is set to 200K
● If the employee does not have a valid salary (set to None in the
setter, perhaps), print diagnostic

'''

class EmployeeWMethods:
    
    def __init__(self, empID, empName, empDept, empSalary):
        self._emp_id = empID
        self._emp_name = empName
        self._emp_dept = empDept
        self._emp_salary = empSalary

    @property
    #getter
    def emp_salary(self):
        return self._emp_salary
    
    #setter
    @emp_salary.setter
    def emp_salary(self, new_salary):
        if 30000 <= new_salary <= 200000:
            self._emp_salary = new_salary
        else:
            self._emp_salary = None
            print(f'Passed value of {new_salary} is not in range. Salary set to None')

    
    def print_me(self):
        print(f'{self._emp_id = }\t{self._emp_name = }\t{self._emp_dept = }\t{self._emp_salary =}')


    def give_emp_pct_raise(self, pct):
        if pct < 10 or pct > 20:
            print(f'Raise percentage {pct} is not in range - no raise was given')
        elif self._emp_salary is None:
            print(f'Employee salary is not set - update salary first')
        else:
            raised_salary = self._emp_salary * (1 + pct/100)
            if raised_salary > 200000:
                self._emp_salary = 200000
            else:
                self._emp_salary = raised_salary

            