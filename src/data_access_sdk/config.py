from dataclasses import dataclass

@dataclass(frozen=True)
class SDKConfig:
    base_url: str
    api_key: str
    timeout_seconds: float = 30.0
    user_agent: str = "data-access-sdk/0.1.0"
