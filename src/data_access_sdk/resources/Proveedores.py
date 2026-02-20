from typing import List, Optional, Dict, Any

from .base import BaseResource
from ..Models.Providers.Proveedor import Proveedor
from ..Validator.proveedor_validators import limpiar_nombre, limpiar_telefono
from ..Common.pagination import Page, normalize_page

class ProveedoresResource(BaseResource):
    _base_path = "/v1/proveedor"

    def get_por_id(self, proveedor_id: int) -> Proveedor:
        payload = self._http.get(f"{self._base_path}/{proveedor_id}")
        return Proveedor.from_dict(payload)

    def listar(self, page: Page = Page()) -> List[Proveedor]:
        p = normalize_page(page)
        payload = self._http.get(self._base_path, params={"page": p.page, "limit": p.limit})
        return [Proveedor.from_dict(x) for x in payload.get("items", [])]

    def buscar_por_nombre(self, query: str, page: Page = Page()) -> List[Proveedor]:
        p = normalize_page(page)
        q = limpiar_nombre(query)
        payload = self._http.get(f"{self._base_path}/buscar/nombre", params={"query": q, "page": p.page, "limit": p.limit})
        return [Proveedor.from_dict(x) for x in payload.get("items", [])]

    def buscar_por_telefono(self, telefono: str, page: Page = Page()) -> List[Proveedor]:
        p = normalize_page(page)
        t = limpiar_telefono(telefono)
        payload = self._http.get(f"{self._base_path}/buscar/telefono", params={"telefono": t, "page": p.page, "limit": p.limit})
        return [Proveedor.from_dict(x) for x in payload.get("items", [])]

    def crear(self, **data: Any) -> Proveedor:
        payload = self._http.post(self._base_path, json=data)
        return Proveedor.from_dict(payload)