code = """import json
import pandas as pd

path = var_call_AOr0c5mpgw70eRNQe74zo8by
with open(path, 'r') as f:
    mongo_records = json.load(f)

sql_records = var_call_CUvfUDUJxN5sHaGFsgk9VbsL

# Ensure sql_records is a list of dicts
if isinstance(sql_records, dict):
    sql_records = [sql_records]

import re
empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    if re.search(r'empirical', text, re.I):
        years = re.findall(r'(19\d{2}|20\d{2})', text)
        pub_year = None
        for y in years:
            y_int = int(y)
            if 1990 <= y_int <= 2025:
                pub_year = y_int
                break
        if pub_year and pub_year > 2016:
            title = re.sub(r'\.txt$', '', filename)
            empirical_papers.append({'title': title, 'year': pub_year})

emp_df = pd.DataFrame(empirical_papers).drop_duplicates(subset=['title']) if empirical_papers else pd.DataFrame(columns=['title','year'])

cit_df = pd.DataFrame(sql_records) if isinstance(sql_records, list) else pd.DataFrame()
if not cit_df.empty and 'total_citations' in cit_df.columns:
    cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, on='title', how='left') if not emp_df.empty else pd.DataFrame(columns=['title','total_citations'])

if not merged.empty:
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    result = merged[['title','total_citations']].to_dict(orient='records')
else:
    result = []

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AOr0c5mpgw70eRNQe74zo8by': 'file_storage/call_AOr0c5mpgw70eRNQe74zo8by.json', 'var_call_CUvfUDUJxN5sHaGFsgk9VbsL': 'file_storage/call_CUvfUDUJxN5sHaGFsgk9VbsL.json'}

exec(code, env_args)
