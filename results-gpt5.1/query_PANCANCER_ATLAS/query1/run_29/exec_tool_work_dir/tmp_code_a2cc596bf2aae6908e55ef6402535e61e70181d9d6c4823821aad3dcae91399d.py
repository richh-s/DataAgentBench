code = """import json, math, re, pandas as pd

# Load full IGF2 expression data
path_expr = var_call_LBfbwcBmoUINgSSegrvwo2Aq
with open(path_expr, 'r') as f:
    expr_data = json.load(f)
expr_df = pd.DataFrame(expr_data)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1).apply(lambda x: math.log10(x))

# Extract patient barcode from Patient_description in clinical data (brain tumors only, but we need LGG specifically)
path_clin_brain = var_call_h295N4dL9FdfZ40LA6qcTVNK
with open(path_clin_brain, 'r') as f:
    clin_data = json.load(f)
clin_df = pd.DataFrame(clin_data)

# Parse TCGA barcode pattern TCGA-..-.... from Patient_description
pattern = re.compile(r"TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}")
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(lambda s: pattern.search(s).group(0) if isinstance(s,str) and pattern.search(s) else None)
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# Restrict to LGG cohort by presence of 'lower grade glioma' or 'Brain lower grade glioma' in description
clin_lgg = clin_df[clin_df['Patient_description'].str.contains('lower grade glioma', case=False, na=False)]

# Exclude histology annotations enclosed in square brackets entirely
clin_lgg = clin_lgg[~clin_lgg['histological_type'].astype(str).str.match(r"^\[.*\]$")]

# Merge expression with clinical LGG
merged = pd.merge(expr_df[['ParticipantBarcode','log10_expr']], clin_lgg[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# Group by histological_type and compute mean log10_expr
result = merged.groupby('histological_type')['log10_expr'].mean().round(4).sort_index()

out = {hist: float(val) for hist, val in result.items()}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_LBfbwcBmoUINgSSegrvwo2Aq': 'file_storage/call_LBfbwcBmoUINgSSegrvwo2Aq.json', 'var_call_3wL5SIpka8GcUeP4p73LeMds': ['clinical_info'], 'var_call_gcS8FGEeEZOSLNPSbGaRpxrU': 'file_storage/call_gcS8FGEeEZOSLNPSbGaRpxrU.json', 'var_call_h295N4dL9FdfZ40LA6qcTVNK': 'file_storage/call_h295N4dL9FdfZ40LA6qcTVNK.json'}

exec(code, env_args)
