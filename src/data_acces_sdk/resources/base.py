from __future__ import annotations

from typing import Any, Dict, Optional
from ..http.client import HttpClient

class BaseResource:
    def __init__(self, http: HttpClient):
        self._http = http

    def _clean_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for k, v in params.items():
            if v is None:
                continue
            out[k] = v
        return out
