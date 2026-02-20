from dataclasses import dataclass

@dataclass(frozen=True)
class Page:
    page: int = 1
    limit: int = 20

def normalize_page(page: Page) -> Page:
    p = page.page if page.page > 0 else 1
    l = page.limit if 1 <= page.limit <= 100 else 20
    return Page(page=p, limit=l)