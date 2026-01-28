code = """import json, re

# var_call_2Ne5MdSFGSf2cVr3c1BFDQ5w is provided in storage as the path to the JSON result
path = var_call_2Ne5MdSFGSf2cVr3c1BFDQ5w
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []

year_re = re.compile(r"(?<!\d)(20\d{2}|19\d{2})(?!\d)")
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    text_lower = text.lower()
    # only consider docs that contain 'physical activity'
    if 'physical activity' not in text_lower:
        continue
    # try to find publication year from the first 1000 chars
    head = text[:1000]
    m = year_re.search(head)
    if not m:
        # search whole document
        m = year_re.search(text)
    year = int(m.group(0)) if m else None
    if year == 2016:
        results.append(title)

# remove duplicates
results = sorted(list(dict.fromkeys(results)))

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_2Ne5MdSFGSf2cVr3c1BFDQ5w': 'file_storage/call_2Ne5MdSFGSf2cVr3c1BFDQ5w.json'}

exec(code, env_args)
