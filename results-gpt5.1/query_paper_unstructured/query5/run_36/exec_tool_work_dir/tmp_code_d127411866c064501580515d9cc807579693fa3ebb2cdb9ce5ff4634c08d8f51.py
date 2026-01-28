code = """import json, re
import pandas as pd

# Load citations data (titles with 2020 citations)
with open(var_call_TaQj5Ee2yzDwLMr5Z6LLqeOM, 'r') as f:
    citations_2020 = json.load(f)

# Load paper docs metadata
with open(var_call_TPK0YzYkTSeOiCDcwn3ZEO2V, 'r') as f:
    paper_docs = json.load(f)

# Build dataframe for paper docs with inferred title and CHI venue flag
rows = []
for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    # title from filename
    title = re.sub(r"\.txt$","", filename)
    # simple CHI venue heuristic: look for "CHI '" or "CHI 20" etc in first 500 chars
    header = text[:500].upper()
    is_chi = ' CHI ' in header or "CHI '" in header or 'CHI,' in header or 'CHI\n' in header
    rows.append({'title': title, 'is_chi': is_chi})

df_docs = pd.DataFrame(rows)

# Citations dataframe
df_cit = pd.DataFrame(citations_2020)

# Join on exact title match
merged = pd.merge(df_cit, df_docs[df_docs['is_chi']], on='title', how='inner')

# Sum total citations for CHI papers
total_citations_chi_2020 = int(merged['total_citations'].astype(int).sum())

result = {'total_citations_for_CHI_papers_cited_in_2020': total_citations_chi_2020}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TaQj5Ee2yzDwLMr5Z6LLqeOM': 'file_storage/call_TaQj5Ee2yzDwLMr5Z6LLqeOM.json', 'var_call_TPK0YzYkTSeOiCDcwn3ZEO2V': 'file_storage/call_TPK0YzYkTSeOiCDcwn3ZEO2V.json'}

exec(code, env_args)
