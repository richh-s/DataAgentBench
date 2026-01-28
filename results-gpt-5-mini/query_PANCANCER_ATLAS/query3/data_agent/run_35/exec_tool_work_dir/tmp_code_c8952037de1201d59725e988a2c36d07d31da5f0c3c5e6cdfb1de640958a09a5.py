code = """import pandas as pd
import re
import json

# Load data from storage-provided file paths
clinical_path = var_call_CpER4D8kxe0emTc45fgMCaUH
mut_path = var_call_hk8JPyVKGwxzlQ9AneWjnDX9

df_clin = pd.read_json(clinical_path)
df_mut = pd.read_json(mut_path)

# Extract barcode from Patient_description
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', text, re.I)
    if m:
        return m.group(1).upper()
    return None

df_clin['barcode'] = df_clin['Patient_description'].astype(str).apply(extract_barcode)

# Filter for records that mention 'breast' in patient_description (case-insensitive)
df_clin['pd_lower'] = df_clin['Patient_description'].astype(str).str.lower()
mask_breast = df_clin['pd_lower'].str.contains('breast') | df_clin['pd_lower'].str.contains('brca')
# Also try to catch 'Breast Invasive' phrasing

# Filter for FEMALE in description
mask_female = df_clin['Patient_description'].astype(str).str.contains('FEMALE', case=False, na=False)

# Known histological types: exclude 'None', '[Not Applicable]', empty or null
bad_hist = set(['None','[Not Applicable]','[Not Available]','Not Reported','Unknown','',None])

def hist_known(x):
    if pd.isna(x):
        return False
    s = str(x).strip()
    if s == '':
        return False
    if s in bad_hist:
        return False
    return True

mask_hist_known = df_clin['histological_type'].apply(hist_known)

# Apply filters
df_brca_female = df_clin[mask_breast & mask_female & mask_hist_known].copy()

# Some rows may not have barcode extracted; drop those
df_brca_female = df_brca_female[df_brca_female['barcode'].notna()].copy()

# Deduplicate by barcode (one patient per barcode)
df_brca_female = df_brca_female.drop_duplicates(subset=['barcode'])

# Prepare mutation set (ParticipantBarcode values)
mut_barcodes = set(df_mut['ParticipantBarcode'].astype(str).str.upper().unique())

# Flag presence of CDH1 mutation
df_brca_female['CDH1_mut'] = df_brca_female['barcode'].apply(lambda x: x in mut_barcodes)

# Build contingency table: histological_type vs CDH1_mut
ct = pd.crosstab(df_brca_female['histological_type'], df_brca_female['CDH1_mut'])
# Ensure both columns True/False present
if True not in ct.columns:
    ct[True] = 0
if False not in ct.columns:
    ct[False] = 0
ct = ct[[True, False]]  # order
ct = ct.rename(columns={True: 'Yes', False: 'No'})

# Exclude histological types with marginal totals <= 10
ct['row_sum'] = ct['Yes'] + ct['No']
ct_included = ct[ct['row_sum'] > 10].drop(columns=['row_sum']).copy()

result = {}
if ct_included.shape[0] == 0:
    result['error'] = 'No histological categories with marginal totals > 10 after filtering; cannot compute chi-square.'
else:
    # Compute chi-square statistic
    observed = ct_included.values.astype(float)
    row_totals = observed.sum(axis=1).reshape(-1,1)
    col_totals = observed.sum(axis=0).reshape(1,-1)
    grand_total = observed.sum()
    expected = (row_totals @ col_totals) / grand_total
    # Avoid division by zero
    with pd.option_context('mode.use_inf_as_na', True):
        chi2 = (((observed - expected) ** 2) / expected).sum()
    # Build output
    result['chi2'] = float(chi2)
    result['grand_total'] = int(grand_total)
    result['included_hist_types'] = list(ct_included.index.astype(str))
    # contingency as dict
    cont_dict = {}
    for idx, row in ct_included.iterrows():
        cont_dict[str(idx)] = {'Yes': int(row['Yes']), 'No': int(row['No'])}
    result['contingency_table'] = cont_dict

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WUTduE6YXwIB0XzZJkiicgTn': ['clinical_info'], 'var_call_raxK4sfkMMSuTsT8liLto0mB': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CpER4D8kxe0emTc45fgMCaUH': 'file_storage/call_CpER4D8kxe0emTc45fgMCaUH.json', 'var_call_hk8JPyVKGwxzlQ9AneWjnDX9': 'file_storage/call_hk8JPyVKGwxzlQ9AneWjnDX9.json'}

exec(code, env_args)
