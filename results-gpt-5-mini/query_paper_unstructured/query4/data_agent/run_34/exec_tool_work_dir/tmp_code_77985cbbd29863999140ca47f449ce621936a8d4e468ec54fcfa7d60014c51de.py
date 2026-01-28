code = """import json, re
# Load Mongo query result from file path variable provided by previous query
path = var_call_mUYLgEizCXXrUtwZaLketBVX
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    text_low = text.lower()
    if 'physical activity' not in text_low:
        continue
    # find years in text (2000-2029)
    years = re.findall(r'(?<!\d)(20\d{2}|19\d{2})(?!\d)', text)
    year = None
    if years:
        # choose earliest occurrence in text
        # find positions
        positions = []
        for y in set(years):
            m = re.search(r'(?<!\d)'+re.escape(y)+r'(?!\d)', text)
            if m:
                positions.append((m.start(), y))
        if positions:
            positions.sort()
            year = int(positions[0][1])
    # fallback: if '2016' anywhere
    if year is None and '2016' in text:
        year = 2016
    if year == 2016:
        titles.append(title)

# unique
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_mUYLgEizCXXrUtwZaLketBVX': 'file_storage/call_mUYLgEizCXXrUtwZaLketBVX.json'}

exec(code, env_args)
