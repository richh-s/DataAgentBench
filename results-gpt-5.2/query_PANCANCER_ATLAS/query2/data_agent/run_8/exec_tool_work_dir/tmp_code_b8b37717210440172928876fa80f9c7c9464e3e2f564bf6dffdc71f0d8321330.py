code = """import json, re
import pandas as pd
from pathlib import Path

# load clinical brca-ish records
p = Path(var_call_Y3Lazastv5JLFldpmjW47dmu)
clinical = pd.read_json(p)
# keep Alive only based on Patient_description text
clinical['alive'] = clinical['Patient_description'].str.contains(r'vital status\s*[:=]?\s*Alive|current vital status\s*[:=]?\s*Alive', case=False, regex=True)
clinical_alive = clinical[clinical['alive']].copy()
# extract participant barcode like TCGA-XX-YYYY
clinical_alive['ParticipantBarcode'] = clinical_alive['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]
clinical_alive = clinical_alive.dropna(subset=['ParticipantBarcode'])

# load CDH1 mutated participant list
p2 = Path(var_call_DC1IZngfhftgWeBRJZHvPPuJ)
mut = pd.read_json(p2)
mut_set = set(mut['ParticipantBarcode'].dropna().unique())
clinical_alive['CDH1_mut'] = clinical_alive['ParticipantBarcode'].isin(mut_set)

# group by histological_type
grp = clinical_alive.groupby('histological_type', dropna=False).agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_cdh1=('CDH1_mut','sum')
).reset_index()
grp['pct_cdh1'] = (grp['n_cdh1'] / grp['n_alive'] * 100).round(2)
# filter histological types with at least 5 alive patients to avoid tiny denominators? not requested; keep all.
# sort by percentage desc then by n_alive desc
res = grp.sort_values(['pct_cdh1','n_alive'], ascending=[False,False]).head(3)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DC1IZngfhftgWeBRJZHvPPuJ': 'file_storage/call_DC1IZngfhftgWeBRJZHvPPuJ.json', 'var_call_NX3IyTbLZM7OY6mBruDlIcGK': ['clinical_info'], 'var_call_Yk9lSarzvHqDzG6laMtGEuwo': 'file_storage/call_Yk9lSarzvHqDzG6laMtGEuwo.json', 'var_call_6h3rri2wB1wwYKucd60qPWyc': [], 'var_call_oxb0WigxSG8zab29hSJpgHV3': [], 'var_call_xNkLFW1I0O0pOnFIUKzsOwM7': [], 'var_call_adedDQ4JLCMfesi6Cwzbw7tG': {'note': 'next step: query all BRCA rows using Patient_description text contains BRCA dataset'}, 'var_call_Y3Lazastv5JLFldpmjW47dmu': 'file_storage/call_Y3Lazastv5JLFldpmjW47dmu.json'}

exec(code, env_args)
