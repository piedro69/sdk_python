from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .base import BaseResource

@dataclass(frozen=True)
class Empleado:
    id: int
    data: Dict[str, Any]

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Empleado":
        emp_id = d.get("id")
        if isinstance(emp_id, int):
            return Empleado(id=emp_id, data=d)
        raise ValueError("Empleado response missing integer field 'id'")

class EmpleadosResource(BaseResource):
    _base_path = "/v1/empleado"

    def get_por_id(self, empleado_id: int) -> Empleado:
        payload = self._http.get(f"{self._base_path}/{empleado_id}")
        if isinstance(payload, dict):
            return Empleado.from_dict(payload)
        raise ValueError("Unexpected response for get_por_id")

    def listar(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        filtros: Optional[Dict[str, Any]] = None,
    ) -> List[Empleado]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if filtros:
            for k, v in filtros.items():
                params[k] = v

        payload = self._http.get(self._base_path, params=self._clean_params(params))

        if isinstance(payload, list):
            return [Empleado.from_dict(x) for x in payload if isinstance(x, dict)]

        if isinstance(payload, dict):
            items = payload.get("items")
            if isinstance(items, list):
                return [Empleado.from_dict(x) for x in items if isinstance(x, dict)]

        raise ValueError("Unexpected response for listar")

    def crear(self, **campos: Any) -> Empleado:
        payload = self._http.post(self._base_path, json=campos)
        if isinstance(payload, dict):
            return Empleado.from_dict(payload)
        raise ValueError("Unexpected response for crear")

    def modificar(self, empleado_id: int, **campos: Any) -> Empleado:
        payload = self._http.patch(f"{self._base_path}/{empleado_id}", json=campos)
        if isinstance(payload, dict):
            return Empleado.from_dict(payload)
        raise ValueError("Unexpected response for modificar")

    def eliminar(self, empleado_id: int) -> None:
        self._http.delete(f"{self._base_path}/{empleado_id}")
