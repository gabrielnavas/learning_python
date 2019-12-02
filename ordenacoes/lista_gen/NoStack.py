class NoStack:
    def __init__(self):
        self._item = None
        self._next = None

    def __init__(self, item, next):
        self._item = item
        self._next = next

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

