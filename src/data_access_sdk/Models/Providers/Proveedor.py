from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Proveedor:
    id: int
    data: Dict[str, Any]

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Proveedor":
        prov_id = d.get("id")
        if isinstance(prov_id, int):
            return Proveedor(id=prov_id, data=d)
        if isinstance(prov_id, str) and prov_id.isdigit():
            return Proveedor(id=int(prov_id), data=d)
        raise ValueError("Proveedor response missing numeric field 'id'")