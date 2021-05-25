class SearchReference(object):
    def __init__(self):
        pass
    
    def check(self, rows, character_count):
        key = self.key.ljust(10, "0")
        if key in rows:
            self.found = True
        else:
            self.found = False
    
 