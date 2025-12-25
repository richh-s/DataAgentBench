code = """import json, pandas as pd, math, re

# Load full IGF2 expression data
with open(var_call_ogxfkyQ2P3pIn0S4ny6kYPOt, 'r') as f:
    igf2_expr = json.load(f)

df_expr = pd.DataFrame(igf2_expr)
# ensure numeric
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
# drop invalid
df_expr = df_expr.dropna(subset=['normalized_count'])

# Extract patient barcode from Patient_description for LGG cohort
with open(var_call_xUS16Vj1UJwzTtOPDyx4kgvI, 'r') as f:
    lgg_clin = json.load(f)

rows = []
for rec in lgg_clin:
    desc = rec['Patient_description']
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if not m:
        continue
    barcode = m.group(0)
    hist = rec.get('histological_type')
    # exclude histology enclosed in square brackets
    if hist is None:
        continue
    h = hist.strip()
    if h.startswith('[') and h.endswith(']'):
        continue
    rows.append({'ParticipantBarcode': barcode, 'histological_type': h})

df_clin = pd.DataFrame(rows).drop_duplicates()

# Merge expression with LGG clinical by ParticipantBarcode
merged = pd.merge(df_expr, df_clin, on='ParticipantBarcode', how='inner')

# compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr'])

result = merged.groupby('histological_type')['log10_expr'].mean().round(4).sort_index()

out = result.reset_index().to_dict(orient='records')

j = json.dumps(out)
print("__RESULT__:")
print(j)"""

env_args = {'var_call_ogxfkyQ2P3pIn0S4ny6kYPOt': 'file_storage/call_ogxfkyQ2P3pIn0S4ny6kYPOt.json', 'var_call_xj1PXkDR2vDawt96gUessLda': ['clinical_info'], 'var_call_Beur4TGJuxqZRfsdsLcLqUcH': 'file_storage/call_Beur4TGJuxqZRfsdsLcLqUcH.json', 'var_call_xUS16Vj1UJwzTtOPDyx4kgvI': 'file_storage/call_xUS16Vj1UJwzTtOPDyx4kgvI.json'}

exec(code, env_args)
