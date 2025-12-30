code = """import json
import pandas as pd

# Load full results from files
with open(var_call_EH4lyvVt6YLpJRrephYjrAjG, 'r') as f:
    citations = json.load(f)
with open(var_call_3ypz0svmlvDcdD0xdptUXenj, 'r') as f:
    chi_docs = json.load(f)

cit_df = pd.DataFrame(citations)
chi_df = pd.DataFrame(chi_docs)

chi_df['title'] = chi_df['filename'].str.replace('.txt', '', regex=False)

merged = cit_df.merge(chi_df[['title']], on='title', how='inner')
merged['citation_count'] = merged['citation_count'].astype(int)

total_citations = int(merged['citation_count'].sum())

import json as json_mod
result = json_mod.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EH4lyvVt6YLpJRrephYjrAjG': 'file_storage/call_EH4lyvVt6YLpJRrephYjrAjG.json', 'var_call_npvOu7svGeeEIF3bB8D9YbzU': ['paper_docs'], 'var_call_3ypz0svmlvDcdD0xdptUXenj': 'file_storage/call_3ypz0svmlvDcdD0xdptUXenj.json'}

exec(code, env_args)
