"""


import requests

BASE_URL = ""








r = requests.get(
    f"{BASE_URL}/test/now",
    headers={"x-api-key": API_KEY}
)

print("status:", r.status_code)
print("body:", r.text)

"""

import requests
import json

BASE_URL = "http://localhost:3000"
#BASE_URL="https://config-data-gateway.onrender.com"
API_KEY = "sk_test_a1e763b8e277fa7c8536290aa3c6893e78c346a12639094f9241aa0fbeba335f"



































