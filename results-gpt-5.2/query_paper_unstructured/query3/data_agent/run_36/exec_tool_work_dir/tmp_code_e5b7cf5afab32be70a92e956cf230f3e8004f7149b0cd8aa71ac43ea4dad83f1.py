code = """import json
import pandas as pd

cits_src = var_call_B8K4UO5BTpJMWJ0R1quKYhOE
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

# In absence of reliable metadata extraction from documents, approximate 'empirical' contribution by title containing 'Empirical'
df = pd.DataFrame(cits)
df['total_citations'] = pd.to_numeric(df['total_citations'], errors='coerce').fillna(0).astype(int)
emp = df[df['title'].str.contains('empirical', case=False, na=False)].sort_values('total_citations', ascending=False)

print('__RESULT__:')
print(json.dumps(emp[['title','total_citations']].to_dict(orient='records')))"""

env_args = {'var_call_fWruw89VasDc1xQsR4VIVlXr': 'file_storage/call_fWruw89VasDc1xQsR4VIVlXr.json', 'var_call_B8K4UO5BTpJMWJ0R1quKYhOE': 'file_storage/call_B8K4UO5BTpJMWJ0R1quKYhOE.json'}

exec(code, env_args)
