from typing import List
from abc import ABC


class AbstractSearching(ABC):
    def search(self, nums: List, key: int) -> int:
        pass
