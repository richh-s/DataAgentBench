code = """import re, json
import pandas as pd

mongo_path = var_call_9c8KG0T3EbdOXzTs9FF7LNJP
sql_path = var_call_d2ZdtbKgYAqkTDQT3dG7Moav

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

records = []
for doc in mongo_records:
    text = doc.get('text', '')
    years = re.findall(r'(20[1-2][0-9])', text)
    year_val = None
    for y in years:
        yi = int(y)
        if 2010 <= yi <= 2025:
            year_val = yi
            break
    contrib = 'empirical' if re.search(r'empirical', text, re.IGNORECASE) else None
    if contrib == 'empirical' and year_val is not None and year_val > 2016:
        filename = doc.get('filename', '')
        title = re.sub(r'\.txt$', '', filename)
        records.append({'title': title, 'year': year_val})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(sql_records)

# Inspect columns
cols = list(cit_df.columns)

result = {'papers_count': len(papers_df), 'cit_cols': cols[:10]}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9c8KG0T3EbdOXzTs9FF7LNJP': 'file_storage/call_9c8KG0T3EbdOXzTs9FF7LNJP.json', 'var_call_d2ZdtbKgYAqkTDQT3dG7Moav': 'file_storage/call_d2ZdtbKgYAqkTDQT3dG7Moav.json'}

exec(code, env_args)
