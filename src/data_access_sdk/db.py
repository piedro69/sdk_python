from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class ApiError(Exception):
    status_code: int
    message: str
    details: Optional[Any] = None
    request_id: Optional[str] = None
    url: Optional[str] = None

    def __str__(self) -> str:
        base = f"[HTTP {self.status_code}] {self.message}"
        if self.request_id:
            base += f" (request_id={self.request_id})"
        if self.url:
            base += f" (url={self.url})"
        return base


class BadRequestError(ApiError):
    pass


class UnauthorizedError(ApiError):
    pass


class ForbiddenError(ApiError):
    pass


class NotFoundError(ApiError):
    pass


class ConflictError(ApiError):
    pass


class RateLimitedError(ApiError):
    pass


class ServerError(ApiError):
    pass


def map_http_error(
    *,
    status_code: int,
    message: str,
    details: Any,
    request_id: Optional[str],
    url: Optional[str],
) -> ApiError:
    if status_code == 400:
        return BadRequestError(status_code, message, details, request_id, url)
    if status_code == 401:
        return UnauthorizedError(status_code, message, details, request_id, url)
    if status_code == 403:
        return ForbiddenError(status_code, message, details, request_id, url)
    if status_code == 404:
        return NotFoundError(status_code, message, details, request_id, url)
    if status_code == 409:
        return ConflictError(status_code, message, details, request_id, url)
    if status_code == 429:
        return RateLimitedError(status_code, message, details, request_id, url)
    if status_code >= 500:
        return ServerError(status_code, message, details, request_id, url)
    return ApiError(status_code, message, details, request_id, url)