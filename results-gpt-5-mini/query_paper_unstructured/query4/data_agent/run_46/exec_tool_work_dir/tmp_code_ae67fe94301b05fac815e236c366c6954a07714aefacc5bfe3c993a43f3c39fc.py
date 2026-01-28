code = """import json, re

# Load the Mongo query result from storage
path = var_call_ueY8ny6tvVKcJ9NNvBSzXQv9
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles_2016_physical = []
for doc in docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    low = text.lower()
    # domain match: contains 'physical activity'
    domain_match = 'physical activity' in low or 'physical-activity' in low
    if not domain_match:
        continue
    # find year by searching for 4-digit years between 1990 and 2026
    matches = list(re.finditer(r"\b(19[5-9][0-9]|20[0-2][0-9]|2026)\b", text))
    year = None
    if matches:
        # choose the earliest occurrence in the document
        first = min(matches, key=lambda m: m.start())
        year = int(first.group(0))
    # consider only year == 2016
    if year == 2016:
        titles_2016_physical.append(title)

# Deduplicate
titles_2016_physical = list(dict.fromkeys(titles_2016_physical))

import json
print("__RESULT__:")
print(json.dumps(titles_2016_physical))"""

env_args = {'var_call_ueY8ny6tvVKcJ9NNvBSzXQv9': 'file_storage/call_ueY8ny6tvVKcJ9NNvBSzXQv9.json'}

exec(code, env_args)
