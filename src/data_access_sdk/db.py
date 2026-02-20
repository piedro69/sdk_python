from __future__ import annotations

from .config import SDKConfig
from .http.client import HttpClient
from .resources.Empleados import EmpleadosResource
from .resources.Proveedores import ProveedoresResource

class DataAccessSDK:
    def __init__(self,api_key: str, *, timeout_seconds: float = 30.0):
        config = SDKConfig(
            base_url="https://config-data-gateway.onrender.com",
            api_key=api_key,
            timeout_seconds=timeout_seconds
        )
        self._http = HttpClient(config)
        self.empleados = EmpleadosResource(self._http)
        self.proveedores=ProveedoresResource(self._http)

    def close(self) -> None:
        self._http.close()
