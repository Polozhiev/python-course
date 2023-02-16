import random
import json

class Salary:
    def __init__(self, cash_size=12):
        self.cash = Cash(cash_size)

    def get(self, input):
        json_dict = json.loads(input)
        date = str(json_dict['year']) + json_dict['month'].strip()
        salary = int(json_dict['salary'])
        if self.cash.get(date):
            json_dict['hour_income'] = self.cash.get(date)
            return json.dumps(json_dict)
        else:
            w_days = random.randint(20, 23)
            hour_income = '{:.2f}'.format(salary/(w_days*8))
            self.cash.add(date, hour_income)
            json_dict['hour_income'] = hour_income
            return json.dumps(json_dict)

class Cash:
    def __init__(self, size=12):
        self.cash = {}
        self.size = size

    def get(self, id):
        return self.cash.get(id)

    def add(self, id, val):
        if id in self.cash.keys():
            pass
        elif len(self.cash) < self.size:
            self.cash[id] = val
        else:
            it = iter(self.cash)
            self.cash.pop(next(it))
            self.cash[id] = val