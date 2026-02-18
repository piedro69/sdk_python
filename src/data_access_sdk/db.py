from __future__ import annotations

from .config import SDKConfig
from .http.client import HttpClient
from .resources.Empleados import EmpleadosResource

class DataAccessSDK:
    def __init__(self, base_url: str, api_key: str, *, timeout_seconds: float = 30.0):
        config = SDKConfig(
            base_url=base_url,
            api_key=api_key,
            timeout_seconds=timeout_seconds
        )
        self._http = HttpClient(config)
        self.empleados = EmpleadosResource(self._http)

    def close(self) -> None:
        self._http.close()
