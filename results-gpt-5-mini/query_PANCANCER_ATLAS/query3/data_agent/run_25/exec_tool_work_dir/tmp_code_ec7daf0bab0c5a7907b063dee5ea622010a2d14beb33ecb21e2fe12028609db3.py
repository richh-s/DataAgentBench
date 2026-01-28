code = """import json
import pandas as pd
import re
import math

# Load query results from storage files
with open(var_call_VvVQRSvpdi0HXeEPaw8ZDQXs, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_O9AYUCWgUs88PDOnD8GWuXmk, 'r') as f:
    mutation_records = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical_records)
df_mut = pd.DataFrame(mutation_records)

# Extract ParticipantBarcode from Patient_description using regex
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[^-]+-[^-]+)', text)
    return m.group(1) if m else None

df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)

# Normalize histological_type
def clean_hist(ht):
    if not isinstance(ht, str):
        return None
    ht_str = ht.strip()
    if ht_str == '' or ht_str.lower().startswith('none') or 'not applicable' in ht_str.lower() or ht_str.lower().startswith('other'):
        return None
    return ht_str

df_clin['hist_clean'] = df_clin['histological_type'].apply(clean_hist)

# Keep only female BRCA patients with known histological type and a ParticipantBarcode
# The query used already filtered by Patient_description containing Breast and FEMALE, but double-check
mask = df_clin['ParticipantBarcode'].notnull() & df_clin['hist_clean'].notnull()
df_clin = df_clin.loc[mask, ['ParticipantBarcode','hist_clean']].drop_duplicates(subset=['ParticipantBarcode'])

# Prepare mutation participant set (only PASS entries already queried)
mut_participants = set(df_mut['ParticipantBarcode'].dropna().astype(str).str.upper().unique())

# Ensure ParticipantBarcode uppercase for matching
df_clin['ParticipantBarcode'] = df_clin['ParticipantBarcode'].str.upper()

# For each histological type, count mutated vs not mutated
grouped = df_clin.groupby('hist_clean')['ParticipantBarcode'].apply(list).to_dict()
contingency = {}
for hist, parts in grouped.items():
    total = len(parts)
    mutated = sum(1 for p in parts if p in mut_participants)
    not_mut = total - mutated
    contingency[hist] = {'Mutated': mutated, 'Not_mutated': not_mut, 'Total': total}

# Exclude histological categories with marginal totals less than or equal to 10
included = {h: v for h, v in contingency.items() if v['Total'] > 10}

# Build contingency table matrix for chi-square: rows are hist types, cols Mutated, Not_mutated
hist_types = sorted(included.keys())
if len(hist_types) == 0:
    result = {'error': 'No histological categories with total > 10 after filtering.'}
else:
    obs = []
    for h in hist_types:
        obs.append([included[h]['Mutated'], included[h]['Not_mutated']])

    # Compute chi-square statistic manually
    obs_arr = pd.DataFrame(obs, columns=['Mutated','Not_mutated'])
    row_totals = obs_arr.sum(axis=1)
    col_totals = obs_arr.sum(axis=0)
    grand_total = col_totals.sum()

    chi2 = 0.0
    expected = []
    for i in range(len(obs_arr)):
        expected_row = []
        for j, col in enumerate(obs_arr.columns):
            Eij = (row_totals.iat[i] * col_totals.iat[j]) / grand_total if grand_total>0 else 0
            expected_row.append(Eij)
            Oij = obs_arr.iat[i,j]
            # Avoid division by zero; if Eij == 0, contribution is 0 (and Oij should be 0)
            if Eij > 0:
                chi2 += (Oij - Eij)**2 / Eij
        expected.append(expected_row)

    # Prepare output
    result = {
        'contingency_table': {h: included[h] for h in hist_types},
        'chi2_statistic': chi2,
        'degrees_of_freedom': (len(hist_types)-1)*(2-1),
        'included_histological_types': hist_types,
        'grand_total_patients_included': int(grand_total)
    }

# Print result following required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6g4YxzleZk0vgjLPKS6FzixP': ['clinical_info'], 'var_call_AFVGpEpRogy2akrYLnpfOVhh': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_sVQolyFdsEirGSgaZ4AUCh2x': 'file_storage/call_sVQolyFdsEirGSgaZ4AUCh2x.json', 'var_call_Snxbn3LzeKEBamIszVqr8kPy': 'file_storage/call_Snxbn3LzeKEBamIszVqr8kPy.json', 'var_call_VvVQRSvpdi0HXeEPaw8ZDQXs': 'file_storage/call_VvVQRSvpdi0HXeEPaw8ZDQXs.json', 'var_call_O9AYUCWgUs88PDOnD8GWuXmk': 'file_storage/call_O9AYUCWgUs88PDOnD8GWuXmk.json'}

exec(code, env_args)
