from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ApiError(Exception):
    status_code: Optional[int]
    message: str
    method: str
    url: str
    response_text: Optional[str] = None

    def __str__(self) -> str:
        sc = self.status_code if self.status_code is not None else "?"
        return f"[{sc}] {self.method} {self.url} - {self.message}"