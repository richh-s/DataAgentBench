code = """import re, json, pandas as pd

# Load full clinical breast dataset
path = var_call_K3uaaOyPXUHCXiCYUXJWN3E3
with open(path, 'r') as f:
    clinical = json.load(f)

clin_df = pd.DataFrame(clinical)

# Keep only females based on Patient_description text
clin_df = clin_df[clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)].copy()

# Extract barcode (Participant ID) from Patient_description (pattern TCGA-..-....)
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-..-....)')
clin_df = clin_df.dropna(subset=['ParticipantBarcode', 'histological_type'])

# Load mutation data for CDH1
path_mut = var_call_KXn8oLliGDWtB1UKmsoS37Lo
with open(path_mut, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)

# Reliable mutations: FILTER == 'PASS'
mut_df = mut_df[mut_df['FILTER'] == 'PASS'].copy()

# Collapse to patient-level mutation presence
mut_patients = mut_df['ParticipantBarcode'].dropna().unique()

# Merge to clinical
clin_df['CDH1_mut'] = clin_df['ParticipantBarcode'].isin(mut_patients)

# Build contingency table of histological_type vs mutation status
cont = pd.crosstab(clin_df['histological_type'], clin_df['CDH1_mut'])

# Exclude categories with any marginal total <= 10
row_totals = cont.sum(axis=1)
col_totals = cont.sum(axis=0)
valid_rows = row_totals[row_totals > 10].index
valid_cols = col_totals[col_totals > 10].index
cont_filt = cont.loc[valid_rows, valid_cols]

# If after filtering we don't have at least 2x2, chi-square is not defined
if cont_filt.size == 0 or cont_filt.shape[0] < 2 or cont_filt.shape[1] < 2:
    result = {'chi_square': None, 'df': None, 'note': 'Insufficient data after applying marginal total >10 filter to construct at least a 2x2 table.', 'contingency_table': cont.to_dict()}
else:
    # Compute chi-square statistic
    grand_total = cont_filt.values.sum()
    row_totals = cont_filt.sum(axis=1).values.reshape(-1,1)
    col_totals = cont_filt.sum(axis=0).values.reshape(1,-1)
    expected = row_totals @ col_totals / grand_total
    observed = cont_filt.values
    chi_sq = ((observed - expected)**2 / expected).sum()
    df = (cont_filt.shape[0]-1)*(cont_filt.shape[1]-1)
    result = {
        'chi_square': float(chi_sq),
        'df': int(df),
        'grand_total': int(grand_total),
        'contingency_table': cont_filt.to_dict(),
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_KXn8oLliGDWtB1UKmsoS37Lo': 'file_storage/call_KXn8oLliGDWtB1UKmsoS37Lo.json', 'var_call_SZx9DozXLyTHTvJDXSX7XSj0': ['clinical_info'], 'var_call_r7RIIxcgUMOXoRGM1189X8jU': 'file_storage/call_r7RIIxcgUMOXoRGM1189X8jU.json', 'var_call_K3uaaOyPXUHCXiCYUXJWN3E3': 'file_storage/call_K3uaaOyPXUHCXiCYUXJWN3E3.json'}

exec(code, env_args)
