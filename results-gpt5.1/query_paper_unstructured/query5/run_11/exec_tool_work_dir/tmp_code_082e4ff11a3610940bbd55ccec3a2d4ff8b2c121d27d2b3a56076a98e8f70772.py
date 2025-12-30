code = """import json, re
import pandas as pd

# Load citations from file path (since it's stored in a file as well)
with open(var_call_Xllr6H03uG83ua2z3KFNSPTq, 'r') as f:
    cts = json.load(f)

# Load full paper_docs result from file path
with open(var_call_vXOuV4VP5xDu7dMtL3aWIUP3, 'r') as f:
    paper_docs = json.load(f)

records = []
for doc in paper_docs:
    fname = doc.get('filename','')
    title = re.sub(r'\.txt$','', fname)
    text = doc.get('text','') or ''
    head = text[:1000].upper()
    venue = 'CHI' if ' CHI ' in head or "CHI '" in head or ' CHI,' in head else None
    records.append({'title': title, 'venue': venue})

df_papers = pd.DataFrame(records)
chi_papers = df_papers[df_papers['venue']=='CHI']
chi_titles = set(chi_papers['title'])

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
