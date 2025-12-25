code = """import json, re, math, pandas as pd

# Load full RNA expression result
with open(var_call_d6VZIVSZK84FbTEr3jw9mhaK, 'r') as f:
    rna = json.load(f)

# Load full LGG clinical result
with open(var_call_9CexvmIEVoZWTwtozXkLQs4f, 'r') as f:
    clin = json.load(f)

# Extract patient barcodes from Patient_description (pattern TCGA-..-....)
barcode_re = re.compile(r"TCGA-..-....")
clin_rows = []
for row in clin:
    m = barcode_re.search(row['Patient_description'])
    if not m:
        continue
    pid = m.group(0)
    hist = row.get('histological_type')
    # Exclude histology enclosed in square brackets like "[Not Available]"
    if hist is None:
        continue
    hist = hist.strip()
    if hist.startswith('[') and hist.endswith(']'):
        continue
    clin_rows.append({'ParticipantBarcode': pid, 'histological_type': hist})

clin_df = pd.DataFrame(clin_rows).drop_duplicates()

rna_df = pd.DataFrame(rna)
# Ensure numeric
rna_df['normalized_count'] = pd.to_numeric(rna_df['normalized_count'], errors='coerce')
# Drop invalid expression
rna_df = rna_df.dropna(subset=['normalized_count'])

# Merge on ParticipantBarcode
merged = pd.merge(rna_df, clin_df, on='ParticipantBarcode', how='inner')

if merged.empty:
    result = {}
else:
    # Compute log10(normalized_count + 1)
    merged['log10_expr'] = (merged['normalized_count'] + 1).map(lambda x: math.log10(x))
    grp = merged.groupby('histological_type')['log10_expr'].mean().sort_index()
    result = {k: round(float(v), 4) for k, v in grp.to_dict().items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d6VZIVSZK84FbTEr3jw9mhaK': 'file_storage/call_d6VZIVSZK84FbTEr3jw9mhaK.json', 'var_call_Nt5PHwLMWyvRe8gvXJmLmnK9': ['clinical_info'], 'var_call_Zn0DrPZRjm2ctjEtTUZV5QB7': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}], 'var_call_9CexvmIEVoZWTwtozXkLQs4f': 'file_storage/call_9CexvmIEVoZWTwtozXkLQs4f.json'}

exec(code, env_args)
