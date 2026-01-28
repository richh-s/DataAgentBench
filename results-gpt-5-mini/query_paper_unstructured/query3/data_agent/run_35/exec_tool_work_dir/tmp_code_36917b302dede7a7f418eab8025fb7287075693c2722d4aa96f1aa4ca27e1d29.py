code = """import json
import re

path = var_call_5Fr9YDfjdx1RAzPDo7Hd08hK
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs[:50]:
    filename = d.get('filename')
    title = None
    if filename:
        title = re.sub(r"\.txt$", "", filename)
    text = d.get('text', '')
    has_empirical = False
    has_empiric = False
    if isinstance(text, str):
        has_empirical = bool(re.search(r"\bempirical\b", text, flags=re.IGNORECASE))
        has_empiric = bool(re.search(r"\bempiric", text, flags=re.IGNORECASE))
    year_match = re.search(r"\b(2017|2018|2019|2020|2021|2022|2023|2024|2025|2026)\b", text)
    year = int(year_match.group(1)) if year_match else None
    results.append({'title': title, 'year': year, 'has_empirical': has_empirical, 'has_empiric': has_empiric})

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_x3lcIfFpwdG8R83HKaR6vCyr': ['paper_docs'], 'var_call_dwPh5YwNHNe5FaYBiOE7aDyC': ['Citations', 'sqlite_sequence'], 'var_call_5Fr9YDfjdx1RAzPDo7Hd08hK': 'file_storage/call_5Fr9YDfjdx1RAzPDo7Hd08hK.json', 'var_call_wLc89tLLAQJxpXJLjZQRx4G8': 'file_storage/call_wLc89tLLAQJxpXJLjZQRx4G8.json', 'var_call_eYYMRXxLVzz1TMLLkatgnom2': []}

exec(code, env_args)
