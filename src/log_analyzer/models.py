from dataclasses import dataclass, field

@dataclass
class LogEntry:
    line_number: int
    content: str

@dataclass
class AnomalyResult:
    pattern: str
    line_numbers: list[int] = field(default_factory=list)

    @property
    def frequency(self) -> int:
        return len(self.line_numbers)
