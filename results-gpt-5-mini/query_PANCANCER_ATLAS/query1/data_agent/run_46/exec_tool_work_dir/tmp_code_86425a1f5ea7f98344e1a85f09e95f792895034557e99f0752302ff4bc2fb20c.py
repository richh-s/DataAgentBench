code = """import json
import pandas as pd

with open(var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L, 'r') as f:
    clinical = json.load(f)

df = pd.DataFrame(clinical)
cols = list(df.columns)
# find columns containing keywords
keywords = ['disease','cancer','project','type','acronym','tumor','site','cohort']
matched = {c: df[c].dropna().astype(str).unique()[:10].tolist() for c in cols if any(k in c.lower() for k in keywords)}

import json as _json
print('__RESULT__:')
print(_json.dumps({'columns': cols, 'matched_samples': matched}))"""

env_args = {'var_call_BnOs3qTuUKJVm1yYaAwIGg6B': ['clinical_info'], 'var_call_Xb1mga1kcDrxacJ3WHx7OOWy': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CQrglBnFJ3kAKzT9XuJNu14U': 'file_storage/call_CQrglBnFJ3kAKzT9XuJNu14U.json', 'var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L': 'file_storage/call_Tfg7buZ6AcKLZPqZ1Zjppr8L.json', 'var_call_SiJXcvDVIVobhLvoiappQcjN': {}}

exec(code, env_args)
