code = """import json
import pandas as pd

# Load the data from storage variables
clinical_var = var_call_iJUudJFix9xP33iQ33jXzH6i
mut_var = var_call_BFbtzQQqg0jHXIVft7gJIKPW

# If the variables are file paths (strings), open and load
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clinical_var

if isinstance(mut_var, str):
    with open(mut_var, 'r') as f:
        mutations = json.load(f)
else:
    mutations = mut_var

# Create DataFrames
df_clin = pd.DataFrame(clinical)
df_mut = pd.DataFrame(mutations)

# Filter clinical: female BRCA patients (Patient_description contains 'breast') and 'FEMALE'
mask_breast = df_clin['Patient_description'].str.contains('breast', case=False, na=False)
mask_female = df_clin['Patient_description'].str.contains('FEMALE', case=False, na=False)
df_brca_female = df_clin[mask_breast & mask_female].copy()

# Keep only known histological types
def known_hist(x):
    if not isinstance(x, str):
        return False
    xs = x.strip().lower()
    if xs in ['', 'none', '[not applicable]', 'unknown']:
        return False
    if xs.startswith('['):
        return False
    if 'other' in xs and 'spec' in xs:  # catches 'Other  specify' variations
        return False
    return True

df_brca_female = df_brca_female[df_brca_female['histological_type'].apply(known_hist)].copy()

# Normalize patient_id to match ParticipantBarcode last segment
df_brca_female['patient_id_norm'] = df_brca_female['patient_id'].astype(str).str.upper().str.strip()

# Prepare mutation data: only PASS entries and Hugo_Symbol == 'CDH1'
if 'FILTER' in df_mut.columns:
    df_mut_pass = df_mut[(df_mut['Hugo_Symbol'] == 'CDH1') & (df_mut['FILTER'] == 'PASS')].copy()
else:
    df_mut_pass = df_mut[df_mut['Hugo_Symbol'] == 'CDH1'].copy()

# Extract patient id from ParticipantBarcode
def extract_pid(pb):
    try:
        return str(pb).split('-')[-1].upper()
    except:
        return str(pb).upper()

if 'ParticipantBarcode' in df_mut_pass.columns:
    df_mut_pass['patient_id_norm'] = df_mut_pass['ParticipantBarcode'].apply(extract_pid)
else:
    df_mut_pass['patient_id_norm'] = df_mut_pass['Tumor_SampleBarcode'].apply(lambda x: extract_pid(x))

# Determine which BRCA female patients have at least one PASS CDH1 mutation
mutated_patients = set(df_mut_pass['patient_id_norm'].unique())

# For each histological type, count mutated and non-mutated
df_brca_female['mutated'] = df_brca_female['patient_id_norm'].apply(lambda x: 1 if x in mutated_patients else 0)

# Build contingency
contingency = df_brca_female.groupby(['histological_type', 'mutated']).size().unstack(fill_value=0)
# Ensure both columns 0 and 1 exist
if 0 not in contingency.columns:
    contingency[0] = 0
if 1 not in contingency.columns:
    contingency[1] = 0
contingency = contingency[[0,1]]

# Exclude histological categories with marginal totals <= 10 (row totals)
contingency['row_total'] = contingency[0] + contingency[1]
contingency_filtered = contingency[contingency['row_total'] > 10].copy()

# If after filtering no rows, return None
if contingency_filtered.shape[0] == 0:
    result = {'chi2': None, 'message': 'No histological categories with total > 10 after filtering.'}
else:
    # Compute chi-square statistic
    grand_total = contingency_filtered[0].sum() + contingency_filtered[1].sum()
    col_totals = {0: contingency_filtered[0].sum(), 1: contingency_filtered[1].sum()}
    chi2 = 0.0
    table = {}
    for idx, row in contingency_filtered.iterrows():
        rtot = row['row_total']
        table[idx] = {'mutated_0': int(row[0]), 'mutated_1': int(row[1]), 'row_total': int(rtot)}
        for col in [0,1]:
            O = row[col]
            E = (rtot * col_totals[col]) / grand_total if grand_total>0 else 0
            if E > 0:
                chi2 += (O - E)**2 / E
    result = {'chi2': chi2, 'grand_total': int(grand_total), 'contingency_filtered': table}

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UqjyoqzmLhxeLwAsqzeVBPkx': ['clinical_info'], 'var_call_6tQnJFmNIEnzIGYsUOflSSEx': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_rzxZ9unUzOe34NJzeMYWFvW5': 'file_storage/call_rzxZ9unUzOe34NJzeMYWFvW5.json', 'var_call_iJUudJFix9xP33iQ33jXzH6i': 'file_storage/call_iJUudJFix9xP33iQ33jXzH6i.json', 'var_call_BFbtzQQqg0jHXIVft7gJIKPW': 'file_storage/call_BFbtzQQqg0jHXIVft7gJIKPW.json'}

exec(code, env_args)
