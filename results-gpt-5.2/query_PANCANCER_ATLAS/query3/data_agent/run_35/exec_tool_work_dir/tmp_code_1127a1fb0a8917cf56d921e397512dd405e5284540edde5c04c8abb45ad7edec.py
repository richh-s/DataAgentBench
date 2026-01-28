code = """import json, re, pandas as pd

# Load clinical records (file path)
path_clin = var_call_NGjzDfU4uxWYWOnXMFMZcXdP
with open(path_clin, 'r') as f:
    clin = json.load(f)

def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

clin_df = pd.DataFrame(clin)
clin_df['participant_barcode'] = clin_df['participant_barcode'].map(extract_barcode)
clin_df = clin_df.dropna(subset=['participant_barcode','histological_type'])
clin_df = clin_df.drop_duplicates(subset=['participant_barcode'])

# Load mutation PASS CDH1 (file path)
path_mut = var_call_lKwWAF7RJT2UW9Pc3t4oFS2A
with open(path_mut, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)
mut_df = mut_df.dropna(subset=['participant_barcode'])
mut_df['cdh1_mut'] = 1
mut_df = mut_df[['participant_barcode','cdh1_mut']].drop_duplicates(subset=['participant_barcode'])

# Join: only female BRCA with known histological types already filtered by query
merged = clin_df.merge(mut_df, on='participant_barcode', how='left')
merged['cdh1_mut'] = merged['cdh1_mut'].fillna(0).astype(int)

# Contingency table: histological_type x mutation status
ct = pd.crosstab(merged['histological_type'], merged['cdh1_mut'])
# ensure both columns present
for c in [0,1]:
    if c not in ct.columns:
        ct[c]=0
ct = ct[[0,1]]

# Exclude categories with marginal totals <= 10 (row totals)
row_totals = ct.sum(axis=1)
ct_f = ct.loc[row_totals > 10].copy()

# Compute chi-square statistic
obs = ct_f.to_numpy(dtype=float)
row_sums = obs.sum(axis=1, keepdims=True)
col_sums = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_sums @ (col_sums / grand)
chi2 = float(((obs - exp)**2 / exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

result = {
    'chi_square': chi2,
    'degrees_of_freedom': dof,
    'grand_total': int(grand),
    'rows_included': int(obs.shape[0]),
    'contingency_table_rows': ct_f.reset_index().rename(columns={'histological_type':'histological_type',0:'CDH1_WT_or_no_PASS',1:'CDH1_MUT_PASS'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lKwWAF7RJT2UW9Pc3t4oFS2A': 'file_storage/call_lKwWAF7RJT2UW9Pc3t4oFS2A.json', 'var_call_OmlDhoMXtoAaVz4JYbQjJCNE': ['clinical_info'], 'var_call_RJGZdHnBcNjx8mU3naAFbuWa': [{'column_name': 'indisexclusion'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}], 'var_call_7gXU46kPrLiTtoYeEWZsbLKw': [], 'var_call_hiFPLm2jicaZdgxdfrvi4nLq': [{'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'patient_death_reason'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'Patient_description'}, {'column_name': 'family_history_of_cancer'}], 'var_call_yrFso9sgCQ6PIFIVZayslnFc': [], 'var_call_aNKDOhKQiksOD8R3ztBzAoNe': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_call_NGjzDfU4uxWYWOnXMFMZcXdP': 'file_storage/call_NGjzDfU4uxWYWOnXMFMZcXdP.json'}

exec(code, env_args)
