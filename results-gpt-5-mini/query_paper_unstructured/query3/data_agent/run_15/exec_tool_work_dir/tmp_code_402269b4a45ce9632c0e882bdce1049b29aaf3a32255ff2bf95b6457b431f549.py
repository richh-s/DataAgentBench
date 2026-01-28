code = """import json, re
# Load the full Mongo query result from storage
path = var_call_koRdw2k2stIYQakj58C4PrJM
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for rec in records:
    filename = rec.get('filename','')
    text = rec.get('text','') or ''
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # find first reasonable year in text (1900-2030)
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    year = None
    for y in years:
        yi = int(y)
        if 1900 <= yi <= 2030:
            year = yi
            break
    # detect contribution type 'empirical' in text
    contribution_found = 'empirical' in text.lower()
    results.append({
        'title': title,
        'year': year,
        'contribution_empirical': contribution_found
    })

# Filter for empirical and year > 2016
filtered = [r for r in results if r['contribution_empirical'] and r['year'] is not None and r['year'] > 2016]

out = {
    'titles': [r['title'] for r in filtered],
    'records': filtered
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hltMAjoVg8naiJZY0LKIVF1Z': ['paper_docs'], 'var_call_koRdw2k2stIYQakj58C4PrJM': 'file_storage/call_koRdw2k2stIYQakj58C4PrJM.json'}

exec(code, env_args)
