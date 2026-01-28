code = """import json, re

# Load the MongoDB query result from storage
path = var_call_jomEIuqLlbvcof8x2J99bnnA
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

candidates = []

for rec in records:
    text = rec.get('text', '')
    filename = rec.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # Check for domain occurrence
    if re.search(r'physical activity', text, re.IGNORECASE):
        # Try to infer publication year from header (first 400 chars)
        header = text[:800]
        year_match = re.search(r'\b(19|20)\d{2}\b', header)
        year = None
        if year_match:
            year = int(year_match.group(0))
        # If header doesn't have year, search broader but prefer header
        if year != 2016:
            # fallback: search for '2016' anywhere but try to ensure it's in a header-like context
            if re.search(r'\b2016\b', text[:2000]):
                year = 2016
        if year == 2016:
            candidates.append(title)

# Deduplicate
candidates = sorted(list(dict.fromkeys(candidates)))

import json
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_call_jomEIuqLlbvcof8x2J99bnnA': 'file_storage/call_jomEIuqLlbvcof8x2J99bnnA.json'}

exec(code, env_args)
