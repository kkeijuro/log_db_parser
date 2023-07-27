from dataclasses import dataclass
from enum import Enum
from typing import Any

class Operation(Enum):
    EQ = 0
    GT = 1
    LT = 2
    GTE = 3
    LTE = 4

@dataclass(frozen=True)
class QFilter:
    attr: str
    value: Any
    operation: Operation

    def operation(self, check_attr) -> bool:
        return check_attr == self.value


