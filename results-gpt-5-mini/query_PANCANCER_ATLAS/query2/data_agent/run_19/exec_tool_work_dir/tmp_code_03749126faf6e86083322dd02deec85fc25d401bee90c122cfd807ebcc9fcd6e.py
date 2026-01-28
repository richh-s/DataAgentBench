code = """import json
import pandas as pd

# Load the clinical and mutation data from storage file paths
with open(var_call_prDEQ4lHK0tE45QP9kkhvXLB, 'r') as f:
    clinical = json.load(f)
with open(var_call_V3oswyYWgXaDgMuk9vN9sN83, 'r') as f:
    mutations = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical)
df_mut = pd.DataFrame(mutations)

# Ensure relevant columns exist
# Extract patient_id from ParticipantBarcode in mutation data (third segment)
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['patient_id'] = df_mut['ParticipantBarcode'].apply(lambda x: x.split('-', 2)[2] if isinstance(x, str) and x.count('-')>=2 else None)
else:
    df_mut['patient_id'] = None

# From clinical dataframe, get unique alive BRCA patients and their histological types
# The clinical query already attempted to filter to BRCA/Breast and Alive, but ensure we consider rows where Patient_description mentions 'Breast' or 'BRCA' and 'Alive'
def is_BRCA_alive(desc):
    if not isinstance(desc, str):
        return False
    desc_low = desc.lower()
    return (('breast' in desc_low or 'brca' in desc_low) and ('alive' in desc_low))

# Filter clinical rows
df_clin['is_brca_alive'] = df_clin['Patient_description'].apply(is_BRCA_alive)
df_clin_br = df_clin[df_clin['is_brca_alive']].copy()

# Use patient_id and histological_type
df_clin_br = df_clin_br[['patient_id', 'histological_type']].dropna()
# Ensure one record per patient (if duplicates, keep first)
df_clin_br = df_clin_br.drop_duplicates(subset=['patient_id'])

# Prepare set of mutated patient ids for CDH1
mutated_patients = set(df_mut['patient_id'].dropna().unique())

# For each histological type, compute total patients and mutated counts
summary = []
for ht, group in df_clin_br.groupby('histological_type'):
    patient_ids = set(group['patient_id'].astype(str).unique())
    total = len(patient_ids)
    if total == 0:
        continue
    mutated = len(patient_ids & mutated_patients)
    pct = (mutated / total) * 100
    summary.append({'histological_type': ht, 'mutated_count': mutated, 'total_count': total, 'percentage': round(pct, 2)})

# Sort by percentage descending and take top 3
summary_sorted = sorted(summary, key=lambda x: x['percentage'], reverse=True)
top3 = summary_sorted[:3]

# Output the result as JSON string
result_str = json.dumps(top3)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_5pLJYq1wVtxagpeMQb54ZVNq': ['clinical_info'], 'var_call_jT50ZgYdHabgIm9fNDKDsDCh': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Csze4R9lxCiHeAo9OI5vlL5V': 'file_storage/call_Csze4R9lxCiHeAo9OI5vlL5V.json', 'var_call_prDEQ4lHK0tE45QP9kkhvXLB': 'file_storage/call_prDEQ4lHK0tE45QP9kkhvXLB.json', 'var_call_V3oswyYWgXaDgMuk9vN9sN83': 'file_storage/call_V3oswyYWgXaDgMuk9vN9sN83.json'}

exec(code, env_args)
