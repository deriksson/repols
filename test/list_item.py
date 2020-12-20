class ListItem:
    value = None

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, ListItem):
            return self.value == other.value
        return False
