code = """import json, re
import pandas as pd

# Load citations (already in memory as var_call_Xllr6H03uG83ua2z3KFNSPTq)
cts = var_call_Xllr6H03uG83ua2z3KFNSPTq

# Load full paper_docs result from file path
with open(var_call_vXOuV4VP5xDu7dMtL3aWIUP3, 'r') as f:
    paper_docs = json.load(f)

# Build helper from filename (without .txt) to venue by regex search in text
records = []
for doc in paper_docs:
    fname = doc.get('filename','')
    title = re.sub(r'\.txt$','', fname)
    text = doc.get('text','') or ''
    # Heuristic: look for CHI in first 1000 chars
    head = text[:1000].upper()
    venue = 'CHI' if ' CHI ' in head or "CHI '" in head or ' CHI,' in head else None
    records.append({'title': title, 'venue': venue})

df_papers = pd.DataFrame(records)

# Filter to CHI papers
chi_papers = df_papers[df_papers['venue']=='CHI']
chi_titles = set(chi_papers['title'])

# Sum citation counts in 2020 for CHI titles
chi_citations_2020 = 0
for row in cts:
    if row['title'] in chi_titles:
        try:
            chi_citations_2020 += int(row['citation_count'])
        except Exception:
            pass

result = chi_citations_2020

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Xllr6H03uG83ua2z3KFNSPTq': 'file_storage/call_Xllr6H03uG83ua2z3KFNSPTq.json', 'var_call_vXOuV4VP5xDu7dMtL3aWIUP3': 'file_storage/call_vXOuV4VP5xDu7dMtL3aWIUP3.json'}

exec(code, env_args)
