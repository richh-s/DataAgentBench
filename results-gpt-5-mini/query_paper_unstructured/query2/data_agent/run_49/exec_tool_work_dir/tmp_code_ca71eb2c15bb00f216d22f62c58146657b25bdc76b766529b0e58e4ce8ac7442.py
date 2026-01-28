code = """import json
import pandas as pd

# Load the query results from storage variables
# var_call_7cKIynMvvnsjUYKOvRIygNAu and var_call_JkyQk4HjUhj2a5khXFv0vRfr are provided by the tool results

# Helper to load JSON if variable is a filepath
def _load_var(v):
    if isinstance(v, str):
        # assume it's a filepath to a .json file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = _load_var(var_call_7cKIynMvvnsjUYKOvRIygNAu)
papers = _load_var(var_call_JkyQk4HjUhj2a5khXFv0vRfr)

# Build set of paper titles from filenames (remove .txt)
titles_set = set()
for d in papers:
    fn = d.get('filename')
    if not fn:
        continue
    if fn.lower().endswith('.txt'):
        titles_set.add(fn[:-4])
    else:
        titles_set.add(fn)

# Create DataFrame for citations
df = pd.DataFrame(citations)
if df.empty:
    avg = None
    total = 0
    count = 0
else:
    # ensure citation_count numeric
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)
    # filter to titles present in titles_set
    df_matched = df[df['title'].isin(titles_set)]
    count = int(len(df_matched))
    total = int(df_matched['citation_count'].sum()) if count>0 else 0
    avg = float(total / count) if count>0 else None

result = {
    'average_citation_count': avg,
    'matching_papers_count': count,
    'total_citations': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7cKIynMvvnsjUYKOvRIygNAu': 'file_storage/call_7cKIynMvvnsjUYKOvRIygNAu.json', 'var_call_JkyQk4HjUhj2a5khXFv0vRfr': 'file_storage/call_JkyQk4HjUhj2a5khXFv0vRfr.json'}

exec(code, env_args)
