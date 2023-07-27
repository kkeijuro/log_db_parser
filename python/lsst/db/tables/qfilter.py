from dataclasses import dataclass
from enum import Enum
from typing import Any

class Operator(Enum):
    EQ = 0
    GT = 1
    LT = 2
    GTE = 3
    LTE = 4

@dataclass(frozen=True)
class QFilter:
    attr: str
    value: Any
    operator: Operator

    def operation(self, check_attr) -> bool:
        if self.operator == Operator.EQ:
            return check_attr == self.value
        elif self.operator == Operator.LT:
            return check_attr < self.value
        elif self.operator == Operator.LTE:
            return check_attr <= self.value
        elif self.operator == Operator.GT:
            return check_attr > self.value
        elif self.operator == Operator.GTE:
            return check_attr >= self.value
        return False


