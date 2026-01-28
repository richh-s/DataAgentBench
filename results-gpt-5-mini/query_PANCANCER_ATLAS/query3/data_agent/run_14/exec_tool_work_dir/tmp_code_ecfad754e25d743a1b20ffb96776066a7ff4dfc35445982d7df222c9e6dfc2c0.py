code = """import json
import pandas as pd

# Load the query results from storage files
with open(var_call_G4KY201qXLDLD7NnACkKfhg2, 'r') as f:
    clinical = json.load(f)
with open(var_call_sDNihSbFExgrvujXqdKLykfu, 'r') as f:
    mutations = json.load(f)

# Create DataFrame
df_clin = pd.DataFrame(clinical)
df_mut = pd.DataFrame(mutations)

# Normalize column names
# clinical patient_id and histological_type
# Filter clinical for entries with known histological_type
def is_known(x):
    if x is None:
        return False
    s = str(x).strip()
    if s == '' or s.upper() in ['NONE', '[NOT APPLICABLE]', '[NOT AVAILABLE]', 'NA', 'N/A']:
        return False
    return True

df_clin = df_clin[df_clin['histological_type'].apply(is_known)].copy()

# Extract patient_id (already present) and ensure uppercase
df_clin['patient_id_norm'] = df_clin['patient_id'].astype(str).str.upper()

# From mutation ParticipantBarcode, extract patient id as third segment
# e.g., TCGA-AC-A5EH -> A5EH
def extract_pid(barcode):
    try:
        parts = str(barcode).split('-')
        if len(parts) >= 3:
            return parts[2].upper()
        else:
            return str(barcode).upper()
    except:
        return str(barcode).upper()

if 'ParticipantBarcode' in df_mut.columns:
    df_mut['patient_id_norm'] = df_mut['ParticipantBarcode'].apply(extract_pid)
else:
    df_mut['patient_id_norm'] = df_mut.iloc[:,0].apply(extract_pid)

# Unique set of mutated patient ids (PASS only already)
mutated_ids = set(df_mut['patient_id_norm'].unique())

# Determine mutation presence for clinical patients
# Only consider female BRCA patients: the clinical query already filtered tumor_tissue_site Breast and FEMALE in Patient_description
# But to be safe, check tumor_tissue_site contains 'Breast' and Patient_description contains 'FEMALE'
if 'tumor_tissue_site' in df_clin.columns:
    df_clin = df_clin[df_clin['tumor_tissue_site'].astype(str).str.contains('Breast', case=False, na=False)]
if 'Patient_description' in df_clin.columns:
    df_clin = df_clin[df_clin['Patient_description'].astype(str).str.contains('FEMALE', case=False, na=False)]

# Map mutated boolean
df_clin['CDH1_mutated'] = df_clin['patient_id_norm'].apply(lambda x: 1 if x in mutated_ids else 0)

# Group by histological_type and build contingency
grouped = df_clin.groupby('histological_type')['CDH1_mutated'].agg(['sum','count']).reset_index()
grouped = grouped.rename(columns={'sum':'mutated','count':'total'})

# Exclude categories with marginal totals <= 10
included = grouped[grouped['total'] > 10].copy()
excluded = grouped[grouped['total'] <= 10]['histological_type'].tolist()

# Build contingency table for included types
contingency = {}
for _, row in included.iterrows():
    ht = row['histological_type']
    mutated = int(row['mutated'])
    total = int(row['total'])
    not_mutated = total - mutated
    contingency[ht] = {'mutated': mutated, 'not_mutated': not_mutated, 'total': total}

# Build matrix for chi-square: rows hist types, cols mutated, not_mutated
import math
rows = list(contingency.keys())
if len(rows) == 0:
    chi2 = None
else:
    matrix = []
    for r in rows:
        matrix.append([contingency[r]['mutated'], contingency[r]['not_mutated']])
    # convert to arrays
    import numpy as np
    mat = np.array(matrix, dtype=float)
    row_totals = mat.sum(axis=1)
    col_totals = mat.sum(axis=0)
    grand_total = mat.sum()
    # compute expected
    expected = np.outer(row_totals, col_totals) / grand_total
    # compute chi2, handle zeros
    with np.errstate(divide='ignore', invalid='ignore'):
        chi2 = float(((mat - expected)**2 / expected).sum())

# Prepare result
result = {
    'chi2': None if chi2 is None else round(chi2, 6),
    'grand_total': int(df_clin.shape[0]),
    'included_histological_types': rows,
    'excluded_histological_types': excluded,
    'contingency': contingency
}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NQNfQOC1vEGlYXwwCMqwNV94': ['clinical_info'], 'var_call_tWlFdPgsaiH6OCFbSxPvb8bl': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0oXnug5QlWtJEn65ShnbpCzy': 'file_storage/call_0oXnug5QlWtJEn65ShnbpCzy.json', 'var_call_sDNihSbFExgrvujXqdKLykfu': 'file_storage/call_sDNihSbFExgrvujXqdKLykfu.json', 'var_call_G4KY201qXLDLD7NnACkKfhg2': 'file_storage/call_G4KY201qXLDLD7NnACkKfhg2.json'}

exec(code, env_args)
