code = """import json, re
import pandas as pd

# load citations 2018
cit_path = var_call_7VyMM00s0l6dMY5QpoWTYjgb
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_c = pd.DataFrame(cit)
df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')
df_c = df_c.dropna(subset=['citation_count'])

# load paper docs
pd_path = var_call_rGO7GnF6LFW28Zr441ko5Wft
with open(pd_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_p = pd.DataFrame(docs)
df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)

# heuristic: ACM if text contains 'Copyright' and 'ACM' or 'Association for Computing Machinery'
pat = re.compile(r'(\bACM\b|Association for Computing Machinery)', re.IGNORECASE)
df_p['is_acm'] = df_p['text'].fillna('').apply(lambda t: bool(pat.search(t)))

# join
merged = df_c.merge(df_p[['title','is_acm']], on='title', how='left')
acm_2018 = merged[merged['is_acm'] == True]

avg_val = float(acm_2018['citation_count'].mean()) if len(acm_2018) else None
n = int(len(acm_2018))

out = {"average_citation_count_2018_acm": avg_val, "num_papers": n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IAteXPITX3zg2Qznu7K02AvT': [{'avg_citations_2018': 'None'}], 'var_call_ZB0jVl2adXVf42an4oZhOcuA': ['Citations', 'sqlite_sequence'], 'var_call_HS0gV60srwtSt7Gde0X4LE6T': ['paper_docs'], 'var_call_7VyMM00s0l6dMY5QpoWTYjgb': 'file_storage/call_7VyMM00s0l6dMY5QpoWTYjgb.json', 'var_call_rGO7GnF6LFW28Zr441ko5Wft': 'file_storage/call_rGO7GnF6LFW28Zr441ko5Wft.json'}

exec(code, env_args)
