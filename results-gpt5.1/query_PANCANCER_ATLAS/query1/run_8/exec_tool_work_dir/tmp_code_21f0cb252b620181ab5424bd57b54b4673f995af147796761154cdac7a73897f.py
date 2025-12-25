code = """import json, math, pandas as pd

# Load full RNA expression
with open(var_call_tCgJd3VNUfuDO9YulfHPg6rl, 'r') as f:
    rna_records = json.load(f)

rna_df = pd.DataFrame(rna_records)

# Extract patient barcode from Patient_description for LGG
with open(var_call_NcEjxslCDVe63zSLAP5N0ABM, 'r') as f:
    clin_records = json.load(f)

clin_df = pd.DataFrame(clin_records)

# Patient_description strings contain 'patient TCGA-XX-YYYY'. Extract that barcode
def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    # find 'patient ' and take next token, or 'Patient '
    for key in ['patient ', 'Patient ']:
        if key in desc:
            part = desc.split(key,1)[1]
            token = part.split(',',1)[0].split(' ',1)[0]
            return token.strip()
    return None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter histology annotations that are not enclosed in square brackets
# i.e., keep rows where histological_type does NOT start with '[' and end with ']'
clin_df = clin_df[clin_df['histological_type'].apply(lambda x: isinstance(x,str) and not (x.startswith('[') and x.endswith(']')))]

# Merge LGG clinical with IGF2 expression
merged = pd.merge(rna_df, clin_df[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# Keep valid normalized_count
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count'])

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1))

# Average per histology type
result_series = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

result = {k: round(float(v), 4) for k, v in result_series.to_dict().items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tCgJd3VNUfuDO9YulfHPg6rl': 'file_storage/call_tCgJd3VNUfuDO9YulfHPg6rl.json', 'var_call_uy3l2JbLcmYlGmlXbPWKIXwF': ['clinical_info'], 'var_call_POUN0lkSasHHFb9DgQvEqSNA': 'file_storage/call_POUN0lkSasHHFb9DgQvEqSNA.json', 'var_call_NcEjxslCDVe63zSLAP5N0ABM': 'file_storage/call_NcEjxslCDVe63zSLAP5N0ABM.json'}

exec(code, env_args)
