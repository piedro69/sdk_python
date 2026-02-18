from dataclasses import dataclass



@dataclass(frozen=True)
class SDKconfig:
    base_url=str
    api_key:str
    timeout_seconds:float=30.0
    user_agent:str="Data/0.1.0"