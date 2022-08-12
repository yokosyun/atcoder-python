class EmploerInfo:
    def __init__(self):
        self.subordinates = []
        self.saraly = 0


n = int(input())
employees = []

for idx in range(n):
    if idx == 0:
        employees.append(EmploerInfo())
    else:
        boss_idx = int(input()) - 1
        employees.append(EmploerInfo())
        employees[boss_idx].subordinates += [idx]
for employee in reversed(employees):
    if len(employee.subordinates) == 0:
        employee.saraly = 1
    else:
        saralies = []
        for idx in employee.subordinates:
            saralies.append(employees[idx].saraly)
        employee.saraly = max(saralies) + min(saralies) + 1

print(employees[0].saraly)
