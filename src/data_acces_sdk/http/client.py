from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, Union
import requests

from ..config import SDKConfig
from .manejo_errores import ApiError, map_http_error

JsonType = Union[Dict[str, Any], list, str, int, float, bool, None]

class HttpClient:
    def __init__(self, config: SDKConfig):
        self._config = config
        self._session = requests.Session()
        self._base_url = self._normalize_base_url(config.base_url)

        self._session.headers.update({
            "x-api-key": config.api_key,
            "User-Agent": config.user_agent,
            "Accept": "application/json",
        })

    def close(self) -> None:
        self._session.close()

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, *, json: Optional[JsonType] = None) -> Any:
        return self._request("POST", path, json=json)

    def put(self, path: str, *, json: Optional[JsonType] = None) -> Any:
        return self._request("PUT", path, json=json)

    def patch(self, path: str, *, json: Optional[JsonType] = None) -> Any:
        return self._request("PATCH", path, json=json)

    def delete(self, path: str, *, json: Optional[JsonType] = None) -> Any:
        return self._request("DELETE", path, json=json)

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[JsonType] = None,
    ) -> Any:
        url = self._build_url(path)

        try:
            resp = self._session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                timeout=self._config.timeout_seconds,
            )
        except requests.RequestException as e:
            raise ApiError(
                status_code=0,
                message=f"Network error: {str(e)}",
                details=None,
                request_id=None,
                url=url,
            )

        if resp.status_code >= 400:
            raise self._to_api_error(resp, url)

        return self._parse_success(resp)

    def _parse_success(self, resp: requests.Response) -> Any:
        if resp.status_code == 204:
            return None
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return resp.json()
        text = resp.text
        if text == "":
            return None
        return text

    def _to_api_error(self, resp: requests.Response, url: str) -> ApiError:
        request_id = resp.headers.get("x-request-id")
        content_type = resp.headers.get("Content-Type", "")

        message, details = self._parse_error_body(resp, content_type)
        return map_http_error(
            status_code=resp.status_code,
            message=message,
            details=details,
            request_id=request_id,
            url=url,
        )

    def _parse_error_body(self, resp: requests.Response, content_type: str) -> Tuple[str, Any]:
        if "application/json" in content_type:
            try:
                data = resp.json()
            except ValueError:
                return (f"HTTP error {resp.status_code}", resp.text)

            msg = self._pick_message(data)
            return (msg, data)

        text = resp.text.strip()
        if text != "":
            return (text, text)
        return (f"HTTP error {resp.status_code}", None)

    def _pick_message(self, data: Any) -> str:
        if isinstance(data, dict):
            if "message" in data and isinstance(data["message"], str):
                return data["message"]
            if "error" in data and isinstance(data["error"], str):
                return data["error"]
            if "detail" in data and isinstance(data["detail"], str):
                return data["detail"]
        return "Request failed"

    def _build_url(self, path: str) -> str:
        cleaned = path.strip()
        if cleaned.startswith("http://") or cleaned.startswith("https://"):
            return cleaned
        if cleaned.startswith("/"):
            return f"{self._base_url}{cleaned}"
        return f"{self._base_url}/{cleaned}"

    def _normalize_base_url(self, base_url: str) -> str:
        u = base_url.strip()
        while u.endswith("/"):
            u = u[:-1]
        return u
