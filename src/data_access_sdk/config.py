from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

DEFAULT_BASE_URL = "https://config-data-gateway.onrender.com"
@dataclass(frozen=True)
class SDKConfig:
    
    api_key: str
    base_url: str= DEFAULT_BASE_URL
    timeout_seconds: float = 30.0
    user_agent: str = "data-access-sdk/0.1.0"
