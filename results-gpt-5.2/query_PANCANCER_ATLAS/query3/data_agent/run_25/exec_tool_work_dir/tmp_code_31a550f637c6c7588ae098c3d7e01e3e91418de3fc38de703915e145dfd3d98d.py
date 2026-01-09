code = """import json, re
import pandas as pd
from pathlib import Path

# Load clinical
p = var_call_RSUaCGLkHddl7kdpmS8IGwA4
clinical = pd.read_json(p)
# extract TCGA barcode
clinical['participant_barcode'] = clinical['patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]
clinical = clinical.dropna(subset=['participant_barcode','histological_type'])
clinical['histological_type'] = clinical['histological_type'].astype(str).str.strip()

# Load mutation participants (CDH1 PASS)
pmut = var_call_PqpLrorFd3BfHgtqY7qwFFPF
mut = pd.read_json(pmut)
mut_set = set(mut['participant_barcode'].dropna().unique().tolist())

# Merge and create mutation presence
clinical['CDH1_mut'] = clinical['participant_barcode'].isin(mut_set)

# Contingency table by histological_type
ct = pd.crosstab(clinical['histological_type'], clinical['CDH1_mut'])
# ensure both columns exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]
ct.columns = ['CDH1_noPASS', 'CDH1_PASS']

# Exclude categories with marginal totals <=10 (row totals)
ct['row_total'] = ct.sum(axis=1)
ct_f = ct[ct['row_total']>10].copy()
ct_f = ct_f.drop(columns=['row_total'])

# Also check column totals >10? apply same rule to columns (marginal totals)
col_totals = ct_f.sum(axis=0)
keep_cols = [c for c in ct_f.columns if col_totals[c]>10]
ct_f2 = ct_f[keep_cols].copy()

# Compute chi-square manually
obs = ct_f2.values.astype(float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ col_tot / grand
chi2 = float(((obs-exp)**2/exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

result = {
  'n_patients_with_known_histology_female_BRCA': int(len(clinical)),
  'n_histology_categories_before_filter': int(ct.shape[0]),
  'contingency_table_used': ct_f2.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records'),
  'chi_square': chi2,
  'degrees_of_freedom': dof,
  'grand_total_used': int(grand)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PqpLrorFd3BfHgtqY7qwFFPF': 'file_storage/call_PqpLrorFd3BfHgtqY7qwFFPF.json', 'var_call_fQbC0gKJszbQ3fBWkKhSoVe5': ['clinical_info'], 'var_call_Pip4ptun5TBx8ujfmNTAnata': 'file_storage/call_Pip4ptun5TBx8ujfmNTAnata.json', 'var_call_ZTdot18lDnDpMr5KZpcZAXhb': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_vhYBsub8GGDs4cUovNNW9aLD': {'next': 'need_query_clinical_with_patient_description_like'}, 'var_call_RSUaCGLkHddl7kdpmS8IGwA4': 'file_storage/call_RSUaCGLkHddl7kdpmS8IGwA4.json'}

exec(code, env_args)
