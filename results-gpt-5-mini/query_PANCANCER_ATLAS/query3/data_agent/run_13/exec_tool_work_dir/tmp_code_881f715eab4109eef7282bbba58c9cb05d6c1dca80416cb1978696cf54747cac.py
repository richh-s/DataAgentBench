code = """import json
import pandas as pd
p = var_call_9ABgWctxsadvEsVX8W4X9wIw
with open(p, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
cols = list(df.columns)
# search for columns that might indicate project or cancer type
candidate_cols = [c for c in cols if any(k in c.lower() for k in ['project','cancer','disease','tumor','site','type','cohort','study','dataset','pan'])]
# check occurrences of BRCA or 'breast' in Patient_description
pd_desc = df['Patient_description'].astype(str)
brca_count = int(pd_desc.str.contains('BRCA', case=False, na=False).sum())
breast_count = int(pd_desc.str.contains('breast', case=False, na=False).sum())

out = {
    'columns': cols,
    'candidate_cols': candidate_cols,
    'patient_description_counts': {'contains_BRCA': nbrca_count, 'contains_breast': breast_count},
    'total_rows': len(df)
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nozhe26iYLtpf3Vr0MbwN4zF': ['clinical_info'], 'var_call_9ABgWctxsadvEsVX8W4X9wIw': 'file_storage/call_9ABgWctxsadvEsVX8W4X9wIw.json'}

exec(code, env_args)
