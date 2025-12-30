code = """import json, pandas as pd

# Load citations data
with open(var_call_Sm3Kq0CAVReVRok9PRb0WLgX, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
cit_df['title'] = cit_df['title'].astype(str)

# Load paper docs
with open(var_call_BB7ElISlmpZTonl0f0kzt3HT, 'r') as f:
    docs = json.load(f)

papers = []
for d in docs:
    fname = d.get('filename','')
    if not fname.lower().endswith('.txt'):
        continue
    title = fname[:-4]
    text = d.get('text','')
    lower = text.lower()
    source = None
    if 'copyright' in lower and 'acm' in lower:
        source = 'ACM'
    elif 'ieee' in lower:
        source = 'IEEE'
    elif 'pubmed' in lower:
        source = 'PubMed'
    papers.append({'title': title, 'source': source})

papers_df = pd.DataFrame(papers)

# Filter ACM papers
acm_papers = papers_df[papers_df['source'] == 'ACM']

# Join with citations
merged = pd.merge(cit_df, acm_papers, on='title', how='inner')
merged['citation_count'] = pd.to_numeric(merged['citation_count'])

avg_citations = merged['citation_count'].mean()

import math, json as js
result = avg_citations if not math.isnan(avg_citations) else None

print("__RESULT__:")
print(js.dumps(result))"""

env_args = {'var_call_Sm3Kq0CAVReVRok9PRb0WLgX': 'file_storage/call_Sm3Kq0CAVReVRok9PRb0WLgX.json', 'var_call_BB7ElISlmpZTonl0f0kzt3HT': 'file_storage/call_BB7ElISlmpZTonl0f0kzt3HT.json'}

exec(code, env_args)
