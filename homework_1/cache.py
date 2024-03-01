from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.memory = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.memory:
            return ""
        self.memory.move_to_end(key)
        return self.memory[key]

    def set(self, key: str, value: str) -> None:
        if key in self.memory:
            self.memory[key] = value
            self.memory.move_to_end(key)
            return

        self.memory[key] = value
        if len(self.memory) == self.capacity:
            self.memory.popitem(last=False)

    def rem(self, key: str) -> None:
        if key in self.memory:
            self.memory.pop(key)
