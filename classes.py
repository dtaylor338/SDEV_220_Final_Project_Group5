from inventory_dictionaries import *


class new_search:
    def __init__(self):
        self.result = []

    def model_search(self, model_var):
        for x in new_inventory:
            for n in new_inventory[x]:
                if n == model_var:
                    self.result.append(new_inventory[x])
        return self.result


    def price_search(self, price_var):
        for x in new_inventory:
            for n in new_inventory[x]:
                if type(n) == int:
                    if n <= price_var:
                        self.result.append(new_inventory[x])
        return self.result



class used_search:
    def __init__(self):
        self.result = []

    def make_search(self, make_var):
        for x in used_inventory:
            for n in used_inventory[x]:
                if n == make_var:
                    self.result.append(used_inventory[x])
        return self.result


    def model_search(self, model_var):
        for x in used_inventory:
            for n in used_inventory[x]:
                if n == model_var:
                    self.result.append(used_inventory[x])
        return self.result


    def year_search(self, year_var):
        for x in used_inventory:
            for n in used_inventory[x]:
                if type(n) == int:
                    if n == year_var:
                        self.result.append(used_inventory[x])
        return self.result

    def price_search(self, price_var):
        for x in used_inventory:
            for n in used_inventory[x]:
                if type(n) == int:
                    if n <= price_var:
                        self.result.append(used_inventory[x])
        return self.result


class all_search:
    def __init__(self):
        self.result = []

    def make_search(self, make_var):
        for x in all_inventory:
            for n in all_inventory:
                if n == make_var:
                    self.result.append(all_inventory[x])
        return self.result


    def model_search(self, make_var):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n == make_var:
                    self.result.append(all_inventory[x])
        return self.result


    def year_search(self, year_var):
        for x in all_inventory:
            for n in all_inventory[x]:
                if type(n) == int:
                    if n == year_var:
                        self.result.append(all_inventory[x])
        return self.result


    def price_search(self, price_var):
        for x in all_inventory:
            for n in all_inventory[x]:
                if type(n) == int:
                    if n <= price_var:
                        self.result = all_inventory[x]
        return self.result


