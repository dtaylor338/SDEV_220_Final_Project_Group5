import inventory_dictionaries




class new_search():
    def __init__(self, model_var, price_var):
        self.model_var = model_var
        self.price_var = price_var

    def model_search(self):
        for x in new_inventory:
            for n in new_inventory[x]:
                if n == self.model_var:
                    result = new_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def price_search(self):
        for x in new_inventory:
            for n in new_inventory[x]:
                if n <= self.price_var:
                    result = new_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result


class used_search():
    def __init__(self, make_var, model_var, year_var, price_var):
        self.make_var = make_var
        self.model_var = model_var
        self.year_var = year_var
        self.price_var = price_var

    def make_search(self):
        for x in used_inventory:
            for n in used_inventory:
                if n == self.model_var:
                    result = used_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def model_search(self):
        for x in used_inventory:
            for n in used_inventory[x]:
                if n == self.model_var:
                    result = used_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def year_search(self):
        for x in used_inventory:
            for n in used_inventory[x]:
                if n == self.year_var:
                    result = used_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def price_search(self):
        for x in used_inventory:
            for n in used_inventory[x]:
                if n <= self.price_var:
                    result = used_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

class all_search():
    def __init__(self, make_var, model_var, year_var, price_var, used_var, new_var):
        self.make_var = make_var
        self.model_var = model_var
        self.year_var = year_var
        self.price_var = price_var
        self.used_var = used_var
        self.new_var = new_var

    def make_search(self):
        for x in all_inventory:
            for n in all_inventory:
                if n == self.model_var:
                    result = all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def model_search(self):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n == self.model_var:
                    result = all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def year_search(self):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n == self.year_var:
                    result = all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def price_search(self):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n <= self.price_var:
                    result = all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

    def usedInv_search(self):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n == self.used_var:
                    result =all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result

def newInv_search(self):
        for x in all_inventory:
            for n in all_inventory[x]:
                if n == self.new_var:
                    result =all_inventory[x]
                    return result
                else:
                    result = 'No vehicles found'
                    return result
