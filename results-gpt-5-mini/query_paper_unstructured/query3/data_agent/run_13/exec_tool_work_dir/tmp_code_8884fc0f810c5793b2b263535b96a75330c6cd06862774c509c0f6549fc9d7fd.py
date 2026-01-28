code = """import json, re
fp = var_call_B722YM6cJSlUDr6ypsTpU1Yg
with open(fp, 'r', encoding='utf-8') as f:
    docs = json.load(f)
matches = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = d.get('text','') or ''
    low = text.lower()
    if 'empir' in low:
        years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
        years_int = [int(y) for y in years if 1900 <= int(y) <= 2026]
        years_int_sorted = sorted(set(years_int))
        first_year = years_int_sorted[0] if years_int_sorted else None
        matches.append({'title': title, 'years_found': years_int_sorted, 'first_year': first_year})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_B722YM6cJSlUDr6ypsTpU1Yg': 'file_storage/call_B722YM6cJSlUDr6ypsTpU1Yg.json', 'var_call_RxOG1HVxK3CTMUeMoESWjDWa': []}

exec(code, env_args)
