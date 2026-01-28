code = """import re, json
import pandas as pd

with open(var_call_KnqHJJ9V657Bwgo93MPhPsCQ, 'r') as f:
    mongo_records = json.load(f)

papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    if not filename:
        continue
    title = filename.replace('.txt', '')

    m = re.search(r'CHI\s*(20\d{2})', text[:5000])
    if not m:
        m = re.search(r'(20\d{2})', text[:1000])
    year = int(m.group(1)) if m else None

    is_empirical = False
    if re.search(r'\bempirical\b', text, re.I):
        is_empirical = True
    else:
        if re.search(r'\b(participants?|interviews?|survey|study|studies|experiment|fieldwork|ethnograph|trial)\b', text, re.I):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        papers.append({'title': title, 'year': year})

with open(var_call_ljjyHD8mSS5ZOtYJgynOZbj8, 'r') as f:
    citation_records = json.load(f)

cit_df = pd.DataFrame(citation_records)

# Inspect columns
cols = list(cit_df.columns)

print("__RESULT__:")
print(json.dumps({'cols': cols, 'sample': cit_df.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_KnqHJJ9V657Bwgo93MPhPsCQ': 'file_storage/call_KnqHJJ9V657Bwgo93MPhPsCQ.json', 'var_call_ljjyHD8mSS5ZOtYJgynOZbj8': 'file_storage/call_ljjyHD8mSS5ZOtYJgynOZbj8.json'}

exec(code, env_args)
