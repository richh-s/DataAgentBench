code = """import json
import pandas as pd

# Load citations data
with open(var_call_0wmg4gdNDOT74VUPCq8aC0eR, 'r') as f:
    citations = json.load(f)

# Load paper docs data
with open(var_call_4ZPWgcGqQsyhBM3jsnKF7JXS, 'r') as f:
    docs = json.load(f)

# Build mapping from title to source (publisher) by parsing text
records = []
for d in docs:
    filename = d.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text', '')
    # Heuristic: if 'ACM' appears near copyright or permission it is ACM source
    source = None
    lower = text.lower()
    if 'copyright' in lower and 'acm' in lower:
        source = 'ACM'
    elif 'acm classification keywords' in lower:
        source = 'ACM'
    elif 'permission to make digital or hard copies' in lower and 'acm' in lower:
        source = 'ACM'
    records.append({'title': title, 'source': source})

paper_df = pd.DataFrame(records)

cit_df = pd.DataFrame(citations)
# citation_count is string in preview; convert to int
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Join on title
merged = cit_df.merge(paper_df, on='title', how='left')

# Filter for ACM source
acm = merged[merged['source'] == 'ACM']

avg_citations = float(acm['citation_count'].mean()) if not acm.empty else None

result = {'average_citation_count_acm_2018': avg_citations, 'paper_count': int(acm.shape[0])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0wmg4gdNDOT74VUPCq8aC0eR': 'file_storage/call_0wmg4gdNDOT74VUPCq8aC0eR.json', 'var_call_4ZPWgcGqQsyhBM3jsnKF7JXS': 'file_storage/call_4ZPWgcGqQsyhBM3jsnKF7JXS.json'}

exec(code, env_args)
