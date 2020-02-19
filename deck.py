import random

class Deck():
    def __init__(self, df, kind, module_name):
        self.type = kind.upper()
        self.items = {}
        self.cards = df.index
        module = __import__(kind.to_lower())
        class_ = getattr(module, kind.capitalize())
        self.items = {name : class_(name, df[name].to_dict()) for name in df.index}
        
    def __repr__(self):
        return 'The {} deck has {} {} left'.format(self.type, len(self.cards), self.type)

    def __str__(self):
        return 'The {} deck has {} {} left'.format(self.type, len(self.cards), self.type)

    def __getitem__(self, key):
        return self.items[key]

    def shuffle(self, times=1):
        for i in range(times):
            random.shuffle(self.cards)

    def draw(self):
        return self.items[self.cards.pop()]
    
    def find(self, key):
        return self.items[key]

    def reshuffle(self):
        self.cards = self.items.keys
        random.shuffle(self.cards)
        return
    
    def remove(self, key):
        if key in self.cards:
                # this throws value error if could not remove or not found
            self.cards.remove(key)
            return self.items[key].reveal().name
        return 'ERROR: {} not found in deck'.format(self.type)

    def debug(self, verbose=False):
        if verbose:
            print('\n'.join([str(self.items[c]) for c in self.cards]))
        else:
            print('\n'.join([c for c in self.cards]))