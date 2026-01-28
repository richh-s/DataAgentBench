code = """import json, re

# Read MongoDB query result from storage variable
fp = var_call_B722YM6cJSlUDr6ypsTpU1Yg
with open(fp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = d.get('text','') or ''
    low = text.lower()
    # Check contribution mention
    if 'empirical' not in low:
        continue
    # Extract first plausible year between 2000 and 2026
    years = re.findall(r"\b(20\d{2}|19\d{2})\b", text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2026:
            year = yi
            break
    if year is None:
        continue
    if year > 2016:
        results.append({'title': title, 'year': year})

titles = [r['title'] for r in results]

print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_call_B722YM6cJSlUDr6ypsTpU1Yg': 'file_storage/call_B722YM6cJSlUDr6ypsTpU1Yg.json'}

exec(code, env_args)
