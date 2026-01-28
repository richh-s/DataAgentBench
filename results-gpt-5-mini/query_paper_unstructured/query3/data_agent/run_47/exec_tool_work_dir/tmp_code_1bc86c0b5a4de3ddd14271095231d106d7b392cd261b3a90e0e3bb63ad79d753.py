code = """import json, re

data_path = var_call_SB2mS1sYxq5FJ9oU82So96qs
if isinstance(data_path, str):
    with open(data_path, 'r', encoding='utf-8') as f:
        papers = json.load(f)
else:
    papers = data_path

rows = []
for doc in papers[:500]:
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt',1)[0] if filename else None
    text = doc.get('text','') or ''
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        years = re.findall(r"\b(20\d{2})\b", text)
        yrs = sorted(list({int(y) for y in years}))
        rows.append({'title': title, 'years_found': yrs})

# Limit output to first 50 entries to keep small
out = rows[:50]
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_cssq7TM9Lb9mcDYNrJdXWaNx': ['paper_docs'], 'var_call_NoWVcXEf50YyN9gDZeLvFtuL': ['Citations', 'sqlite_sequence'], 'var_call_SB2mS1sYxq5FJ9oU82So96qs': 'file_storage/call_SB2mS1sYxq5FJ9oU82So96qs.json', 'var_call_3ey4XApfW9pioL2TAv8w2ENR': 'file_storage/call_3ey4XApfW9pioL2TAv8w2ENR.json', 'var_call_09f5ufuBji0KzkmUe9xFxVAw': []}

exec(code, env_args)
