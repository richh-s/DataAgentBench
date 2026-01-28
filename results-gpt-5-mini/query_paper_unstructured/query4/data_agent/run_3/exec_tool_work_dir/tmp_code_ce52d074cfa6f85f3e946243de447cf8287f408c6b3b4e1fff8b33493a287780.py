code = """import json
import re

# Load the Mongo query result JSON file path from storage variable
data_path = var_call_my4cpHWXG9tLcDQhQAOuLRX4

with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for rec in records:
    filename = rec.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text', '')
    # check domain substring
    if re.search(r'physical activity', text, re.IGNORECASE):
        # search for publication year in first 800 characters, fallback to whole text
        head = text[:800]
        m = re.search(r'\b(20\d{2})\b', head)
        if not m:
            m = re.search(r'\b(20\d{2})\b', text)
        year = int(m.group(1)) if m else None
        if year == 2016:
            results.append(title)

# Deduplicate and sort
unique_titles = sorted(list(dict.fromkeys(results)))

import json
print("__RESULT__:")
print(json.dumps(unique_titles))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json'}

exec(code, env_args)
