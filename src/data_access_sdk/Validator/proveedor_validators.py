import re

def limpiar_nombre(v: str) -> str:
    s = (v or "").strip()
    s = re.sub(r"\s+", " ", s)
    if not (1 <= len(s) <= 50):
        raise ValueError("nombre fuera de rango")
    if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s\.\-]+$", s):
        raise ValueError("nombre invalido")
    return s

def limpiar_telefono(v: str) -> str:
    s = (v or "").strip()
    s = re.sub(r"[^\d+]", "", s)
    if not (3 <= len(s) <= 30):
        raise ValueError("telefono fuera de rango")
    return s