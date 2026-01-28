code = """import json, re
import pandas as pd

with open(var_call_TaQj5Ee2yzDwLMr5Z6LLqeOM, 'r') as f:
    citations_2020 = json.load(f)

with open(var_call_TPK0YzYkTSeOiCDcwn3ZEO2V, 'r') as f:
    paper_docs = json.load(f)

rows = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = re.sub(r'\.txt$', '', filename)
    header = text[:500].upper()
    is_chi = ' CHI ' in header or "CHI '" in header or 'CHI,' in header or 'CHI\n' in header
    rows.append({'title': title, 'is_chi': is_chi})

df_docs = pd.DataFrame(rows)

df_cit = pd.DataFrame(citations_2020)

merged = pd.merge(df_cit, df_docs[df_docs['is_chi']], on='title', how='inner')

if not merged.empty:
    total_citations_chi_2020 = int(merged['total_citations'].astype(int).sum())
else:
    total_citations_chi_2020 = 0

result = {'total_citations_for_CHI_papers_cited_in_2020': total_citations_chi_2020}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TaQj5Ee2yzDwLMr5Z6LLqeOM': 'file_storage/call_TaQj5Ee2yzDwLMr5Z6LLqeOM.json', 'var_call_TPK0YzYkTSeOiCDcwn3ZEO2V': 'file_storage/call_TPK0YzYkTSeOiCDcwn3ZEO2V.json'}

exec(code, env_args)
