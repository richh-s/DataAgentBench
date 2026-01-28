code = """import json
import re

# Load the second Mongo query result
data_path = var_call_JuO8CNjwWTm7g9Dao0RwAxV8
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Extract candidates that likely have year 2016 in text
candidates = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    # domain check
    if re.search(r'physical', text, re.IGNORECASE) and re.search(r'activity', text, re.IGNORECASE):
        # find year near top first 1000 chars
        head = text[:1000]
        m = re.search(r"\b(20\d{2})\b", head)
        year = int(m.group(1)) if m else None
        candidates.append({'title': title, 'year': year, 'filename': filename})

# Show those where year is 2016 or year unknown
filtered = [c for c in candidates if c['year']==2016 or c['year'] is None]

print("__RESULT__:")
print(json.dumps(filtered))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json', 'var_call_wcx4tBKeuw3a6wgVjWKk4E4i': [], 'var_call_JuO8CNjwWTm7g9Dao0RwAxV8': 'file_storage/call_JuO8CNjwWTm7g9Dao0RwAxV8.json'}

exec(code, env_args)
