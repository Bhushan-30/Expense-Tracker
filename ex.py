class expense:
    def __init__(self, name, amt, cat):
        self.name = name
        self.amount = amt
        self.category = cat

    def __repr__(self):
        return f'{self.name},{self.amount:.2f},{self.category}'
