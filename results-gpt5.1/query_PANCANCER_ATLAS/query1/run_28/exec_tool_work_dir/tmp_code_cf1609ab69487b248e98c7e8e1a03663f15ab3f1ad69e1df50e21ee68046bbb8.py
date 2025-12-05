code = """import json, re, math, pandas as pd

# Load data
with open(var_call_Z2eoU3ay1ykDtpWiYtWW8uCI, 'r') as f:
    igf2 = json.load(f)
with open(var_call_n4EeMBuELT0p4RjhWOyluhIi, 'r') as f:
    lgg = json.load(f)

# Map barcode from Patient_description using regex
barcode_pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}')
rows = []
for rec in lgg:
    desc = rec.get('Patient_description','')
    m = barcode_pattern.search(desc)
    if not m:
        continue
    barcode = m.group(0)
    rows.append({'ParticipantBarcode': barcode, 'histological_type': rec.get('histological_type')})

clin_df = pd.DataFrame(rows).drop_duplicates(subset=['ParticipantBarcode'])

igf2_df = pd.DataFrame(igf2)

# Keep valid normalized_count
igf2_df = igf2_df[igf2_df['normalized_count'].notna()]
igf2_df['normalized_count'] = igf2_df['normalized_count'].astype(float)

# Merge LGG clinical with IGF2 expression
merged = pd.merge(clin_df, igf2_df, on='ParticipantBarcode', how='inner')

# Exclude histology enclosed in square brackets
mask_valid_hist = ~merged['histological_type'].astype(str).str.match(r'^\[.*\]$')
merged = merged[mask_valid_hist]

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x))

# Group by histology and compute mean
res = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

out = {hist: round(val, 4) for hist, val in res.items()}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Z2eoU3ay1ykDtpWiYtWW8uCI': 'file_storage/call_Z2eoU3ay1ykDtpWiYtWW8uCI.json', 'var_call_8oyGS0wlB4sNgAK46XCQcCuv': ['clinical_info'], 'var_call_6TVJ9vVGVq83HsDo8XbQT4hW': 'file_storage/call_6TVJ9vVGVq83HsDo8XbQT4hW.json', 'var_call_8Tj8ijyCuMa8IVLoEiJ1zOcc': {'n_igf2_samples': 496, 'n_unique_barcodes': 496}, 'var_call_n4EeMBuELT0p4RjhWOyluhIi': 'file_storage/call_n4EeMBuELT0p4RjhWOyluhIi.json'}

exec(code, env_args)
