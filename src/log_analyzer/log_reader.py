
from pathlib import Path
from .models import LogEntry


class LogReader:

    def read(self, file_path: str) -> list[LogEntry]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

        entries = []

        with path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                entries.append(
                    LogEntry(
                        line_number=line_number,
                        content=line.rstrip("\r\n")
                    )
                )

        return entries
