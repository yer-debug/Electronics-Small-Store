# Class
class Electronics:
    def __init__(self, comp_type, value=None):
        self.comp_type = comp_type
        self.value = value
    
    def __str__(self):
        return f"{self.comp_type}: {self.value}"
