# data-access-sdk

SDK oficial en Python para consumir el **Data Access Service centralizado** (NestJS).
- No permite SQL
- API Key automática en `x-api-key`
- Cliente HTTP central con `requests.Session`
- Errores HTTP -> excepciones Python
- Diseño por dominios (resources) para escalar módulos

## Instalación local
```bash
pip install -e .
