code = """import json, re, pandas as pd
from pathlib import Path

# Load full books data
path = Path(var_call_tOUdm6RV9jzUYiES0dAT6dHM)
with open(path, 'r') as f:
    books = json.load(f)

# Extract publication year from details
rows = []
for b in books:
    details = b.get('details') or ''
    # Look for patterns like 'on January 1, 2004' or 'on March 20, 1995' or 'in January 2004'
    m = re.search(r'on [A-Za-z]+ \d{1,2}, (\d{4})', details)
    if not m:
        m = re.search(r'on (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})', details)
    if not m:
        m = re.search(r'on [A-Za-z]+,? (\d{4})', details)
    if not m:
        m = re.search(r'on .*?(\d{4})', details)
    if not m:
        m = re.search(r'January 1, (\d{4})', details)
    year = None
    if m:
        # last group that looks like a year
        for g in m.groups()[::-1]:
            if g and re.fullmatch(r'\d{4}', g):
                year = int(g)
                break
    if year is None:
        # fallback: any 4-digit year between 1900 and 2025
        m2 = re.findall(r'(\d{4})', details)
        for g in m2:
            y = int(g)
            if 1900 <= y <= 2025:
                year = y
                break
    if year is not None:
        decade = (year // 10) * 10
        rows.append({'book_id': b['book_id'], 'year': year, 'decade': decade})

result = pd.DataFrame(rows).to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_tOUdm6RV9jzUYiES0dAT6dHM': 'file_storage/call_tOUdm6RV9jzUYiES0dAT6dHM.json'}

exec(code, env_args)
