code = """import json, re, math
import pandas as pd

# Load clinical (brain site) and expression
clin_path = var_call_MKQEHN5GG8W8pu0OnU6rpfQ6
expr_path = var_call_rBQw0dYPw33SXXFtP3ooyCyl

with open(clin_path, 'r', encoding='utf-8') as f:
    clin = json.load(f)
with open(expr_path, 'r', encoding='utf-8') as f:
    expr = json.load(f)

dfc = pd.DataFrame(clin)
dfe = pd.DataFrame(expr)

# Extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
dfc['ParticipantBarcode'] = dfc['participantbarcode'].apply(lambda x: (pat.search(x).group(1) if isinstance(x,str) and pat.search(x) else None))
dfc = dfc[['ParticipantBarcode','histology']].rename(columns={'histology':'Histology'}).dropna(subset=['ParticipantBarcode','Histology'])

# Keep LGG only by restricting histology types typical for LGG and excluding GBM explicit
# Since the database lacks cancer acronym, approximate LGG by excluding any histology containing 'GBM' or 'Glioblastoma'
mask_lgg = ~dfc['Histology'].str.contains('GBM|Glioblastoma', case=False, na=False)
dfc = dfc[mask_lgg]

# Histology not enclosed in square brackets already filtered by SQL; ensure again
mask_brackets = ~dfc['Histology'].str.match(r'^\[.*\]$')
dfc = dfc[mask_brackets]

# Expression
# Ensure numeric

dfe['normalized_count'] = pd.to_numeric(dfe['normalized_count'], errors='coerce')
dfe = dfe.dropna(subset=['ParticipantBarcode','normalized_count'])

# If multiple samples per patient for IGF2, average per patient first
per_pat = dfe.groupby('ParticipantBarcode', as_index=False)['normalized_count'].mean()
per_pat['log10_expr'] = (per_pat['normalized_count'] + 1.0).apply(lambda v: math.log10(v) if v>=0 else float('nan'))
per_pat = per_pat.dropna(subset=['log10_expr'])

# Join
merged = pd.merge(dfc, per_pat[['ParticipantBarcode','log10_expr']], on='ParticipantBarcode', how='inner')

res = merged.groupby('Histology', as_index=False)['log10_expr'].mean()
res['avg_log10_IGF2'] = res['log10_expr'].map(lambda v: f"{v:.4f}")
res = res.drop(columns=['log10_expr']).sort_values('Histology')

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rBQw0dYPw33SXXFtP3ooyCyl': 'file_storage/call_rBQw0dYPw33SXXFtP3ooyCyl.json', 'var_call_sJTRY5ELHKvVQpNX3GvJ59Pv': [{'column_name': 'Patient_description'}, {'column_name': 'histological_type'}], 'var_call_ZwacUNiZJ9DuXURN67LRWHWZ': [], 'var_call_yQtb6q8352r9HUWTR2tpXRRF': [], 'var_call_cURxRkAcvRpMhH9KuBamzz1S': [], 'var_call_PU7XBmqwnz1R4kX6lyhpfPAc': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_064uYOcYI9WCyuK8iz7Oxk2o': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_MKQEHN5GG8W8pu0OnU6rpfQ6': 'file_storage/call_MKQEHN5GG8W8pu0OnU6rpfQ6.json'}

exec(code, env_args)
