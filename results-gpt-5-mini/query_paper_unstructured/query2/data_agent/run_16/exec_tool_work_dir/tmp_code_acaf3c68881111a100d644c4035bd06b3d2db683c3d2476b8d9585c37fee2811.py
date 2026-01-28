code = """import json
import pandas as pd

# Load data
with open(var_call_zzK7bHkUDPkIkcg5doQqoM3J, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_9CZg5hl05BZC3LJ77dMjEb4k, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# DataFrames
df_cit = pd.DataFrame(citations)
df_pap = pd.DataFrame(papers)

# Ensure citation_count numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Extract title from filename simply
if 'filename' in df_pap.columns:
    def title_from_filename(x):
        if not isinstance(x, str):
            return x
        if x.lower().endswith('.txt'):
            return x[:-4]
        return x
    df_pap['title'] = df_pap['filename'].apply(title_from_filename)
else:
    df_pap['title'] = None

# Merge
df_merged = pd.merge(df_cit, df_pap[['title', 'text']], on='title', how='left')

# simple ACM detect: 'acm' substring in text (case-insensitive)
df_merged['is_acm'] = df_merged['text'].apply(lambda s: isinstance(s, str) and ('acm' in s.lower()))

# Filter ACM rows
df_acm = df_merged[df_merged['is_acm'] == True]

# Compute average
if len(df_acm) > 0:
    avg = float(df_acm['citation_count'].mean())
    num = int(len(df_acm))
else:
    avg = None
    num = 0

result = {'average_citation_count': avg, 'num_papers_considered': num}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DeTvufNC96JvlW2cJS5cVew7': ['paper_docs'], 'var_call_NLpSfxNXV8s4NEdNNZxjZu5X': ['Citations', 'sqlite_sequence'], 'var_call_zzK7bHkUDPkIkcg5doQqoM3J': 'file_storage/call_zzK7bHkUDPkIkcg5doQqoM3J.json', 'var_call_9CZg5hl05BZC3LJ77dMjEb4k': 'file_storage/call_9CZg5hl05BZC3LJ77dMjEb4k.json', 'var_call_CC5DmtI1pHkPuxfd41fnz36J': {'average_citation_count': None, 'num_papers_considered': 0}}

exec(code, env_args)
