code = """import json, pandas as pd
cdh1_mut = var_call_MK1NAgFpAtCHydun4orMOH1X
if isinstance(cdh1_mut, str) and cdh1_mut.endswith('.json'):
    with open(cdh1_mut, 'r') as f:
        cdh1_mut = json.load(f)

alive_breast = var_call_2TF9LsUp0JlsRo3YxMPsMuEQ
if isinstance(alive_breast, str) and alive_breast.endswith('.json'):
    with open(alive_breast, 'r') as f:
        alive_breast = json.load(f)

# extract patient barcodes from Patient_description, pattern 'TCGA-..-....'
import re
pat = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}')

rows = []
for rec in alive_breast:
    m = pat.search(rec['Patient_description'])
    if not m:
        continue
    barcode = m.group(0)
    rows.append({'ParticipantBarcode': barcode, 'histological_type': rec['histological_type']})

clin_df = pd.DataFrame(rows).drop_duplicates('ParticipantBarcode')
mut_df = pd.DataFrame(cdh1_mut).drop_duplicates('ParticipantBarcode')

# flag mutation per patient
mut_df['CDH1_mut'] = True
merged = clin_df.merge(mut_df[['ParticipantBarcode','CDH1_mut']], on='ParticipantBarcode', how='left')
merged['CDH1_mut'] = merged['CDH1_mut'].fillna(False)

# compute percentage by histological type
summary = merged.groupby('histological_type')['CDH1_mut'].agg(['mean','count','sum']).reset_index()
summary = summary[summary['count']>=1]
summary['percent_mutated'] = summary['mean']*100
summary = summary.sort_values('percent_mutated', ascending=False).head(3)

result = summary[['histological_type','percent_mutated','sum','count']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MK1NAgFpAtCHydun4orMOH1X': 'file_storage/call_MK1NAgFpAtCHydun4orMOH1X.json', 'var_call_K4ojSbJNr2sRlNZu2nZAhB3k': ['clinical_info'], 'var_call_e5XoTniKotfhl1evyqIwfgYy': 'file_storage/call_e5XoTniKotfhl1evyqIwfgYy.json', 'var_call_DMqZtl8PTkC7ggpNEAmlPJ4V': [], 'var_call_2TF9LsUp0JlsRo3YxMPsMuEQ': 'file_storage/call_2TF9LsUp0JlsRo3YxMPsMuEQ.json'}

exec(code, env_args)
