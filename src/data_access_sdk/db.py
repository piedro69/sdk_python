from __future__ import annotations

from .config import SDKconfig
from .http.client import HttpClient


class DataAccessSdk:
    def __init__(
            self,
            base_url:str,    
            api_key:str,
            *,
            timeout_seconds:float=30.0
    ):
        config=SDKconfig(
            base_url=base_url,
            api_key=api_key,
            timeout_seconds=timeout_seconds
        )   
        self._http=HttpClient(config);

    def closedAccess(self)->None:
        self._http.close()
