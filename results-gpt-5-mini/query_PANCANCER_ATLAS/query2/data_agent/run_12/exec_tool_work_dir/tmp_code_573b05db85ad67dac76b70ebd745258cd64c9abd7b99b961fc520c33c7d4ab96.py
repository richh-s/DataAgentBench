code = """import json
import pandas as pd
import re

# Load clinical data (may be a file path)
clinical_var = var_call_thlwv9ZN3HUsxLjUQwu1kHdI
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clinical_var

# Load mutation data
mut_var = var_call_pS5ryuNsoPPdo1WknnvYa2V4
if isinstance(mut_var, str):
    with open(mut_var, 'r') as f:
        mutations = json.load(f)
else:
    mutations = mut_var

# Create DataFrames
df_clin = pd.DataFrame(clinical)
df_mut = pd.DataFrame(mutations)

# Filter clinical rows for Alive only (Patient_description contains 'Alive' case-insensitive)
df_clin_alive = df_clin[df_clin['Patient_description'].str.contains(r'vital status\s*[:=]?\s*Alive', case=False, na=False) | df_clin['Patient_description'].str.contains('\bAlive\b', case=False, na=False)]

# Extract participant barcode using regex TCGA-XX-XXXX or TCGA-XXX-XXXX patterns
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,5})', text)
    if m:
        return m.group(1)
    m2 = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,5}-[A-Za-z0-9]+)', text)
    if m2:
        return m2.group(1)
    return None

# Apply extraction
df_clin_alive['ParticipantBarcode'] = df_clin_alive['Patient_description'].apply(extract_barcode)

# Drop rows without barcode
df_clin_alive = df_clin_alive.dropna(subset=['ParticipantBarcode'])

# Standardize barcodes to upper-case
df_clin_alive['ParticipantBarcode'] = df_clin_alive['ParticipantBarcode'].str.upper()

# Prepare mutation set for CDH1 mutated participants
# df_mut contains ParticipantBarcode entries; ensure uppercase and strip
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].str.upper()
    # Keep unique participants with CDH1
    mutated_participants = set(df_mut['ParticipantBarcode'].unique())
else:
    mutated_participants = set()

# Now group by histological_type: total alive, mutated count
summary = []
for ht, group in df_clin_alive.groupby('histological_type'):
    total = len(group)
    mutated = group['ParticipantBarcode'].isin(mutated_participants).sum()
    pct = (mutated / total * 100) if total > 0 else 0.0
    summary.append({'histological_type': ht, 'total_alive': int(total), 'mutated_count': int(mutated), 'percentage': round(pct, 2)})

# Create DataFrame and pick top 3 by percentage, with at least 1 patient
df_sum = pd.DataFrame(summary)
if df_sum.empty:
    top3 = []
else:
    df_sum = df_sum.sort_values(by=['percentage', 'mutated_count'], ascending=[False, False])
    top3 = df_sum.head(3).to_dict(orient='records')

# Output result as JSON string
result = json.dumps(top3)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_T5Rp3GdyQzeRgW43YOtJgPB0': ['clinical_info'], 'var_call_FftudcLhUAdE9mZKQI5ITKPR': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_GSv7TDqCKGJOfdI5XHM9UQKN': 'file_storage/call_GSv7TDqCKGJOfdI5XHM9UQKN.json', 'var_call_pS5ryuNsoPPdo1WknnvYa2V4': 'file_storage/call_pS5ryuNsoPPdo1WknnvYa2V4.json', 'var_call_aeqAZCwS6G8geGDrmXQZVC42': [], 'var_call_thlwv9ZN3HUsxLjUQwu1kHdI': 'file_storage/call_thlwv9ZN3HUsxLjUQwu1kHdI.json'}

exec(code, env_args)
