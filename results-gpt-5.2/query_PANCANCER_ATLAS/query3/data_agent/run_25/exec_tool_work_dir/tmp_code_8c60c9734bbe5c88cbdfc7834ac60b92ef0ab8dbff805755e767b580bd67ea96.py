code = """import json, pandas as pd

p = var_call_RSUaCGLkHddl7kdpmS8IGwA4
clinical = pd.read_json(p)
clinical['participant_barcode'] = clinical['patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]
clinical = clinical.dropna(subset=['participant_barcode','histological_type'])
clinical['histological_type'] = clinical['histological_type'].astype(str).str.strip()

pmut = var_call_PqpLrorFd3BfHgtqY7qwFFPF
mut = pd.read_json(pmut)
mut_set = set(mut['participant_barcode'].dropna().unique().tolist())
clinical['CDH1_mut'] = clinical['participant_barcode'].isin(mut_set)

ct = pd.crosstab(clinical['histological_type'], clinical['CDH1_mut'])
ct_row = ct[ct.sum(axis=1) > 10].copy()
col_keep = (ct_row.sum(axis=0) > 10)
ct_f = ct_row.loc[:, col_keep].copy()

obs = ct_f.to_numpy(dtype=float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ col_tot / grand
chi2 = float(((obs-exp)**2/exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

ct_out = ct_f.reset_index()
ct_out.columns = ['histological_type'] + [str(c) for c in ct_f.columns]

result = {
  'chi_square': chi2,
  'degrees_of_freedom': dof,
  'grand_total_used': int(grand),
  'n_histology_categories_after_filter': int(ct_f.shape[0]),
  'columns_used': [str(c) for c in ct_f.columns],
  'contingency_table_used': ct_out.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PqpLrorFd3BfHgtqY7qwFFPF': 'file_storage/call_PqpLrorFd3BfHgtqY7qwFFPF.json', 'var_call_fQbC0gKJszbQ3fBWkKhSoVe5': ['clinical_info'], 'var_call_Pip4ptun5TBx8ujfmNTAnata': 'file_storage/call_Pip4ptun5TBx8ujfmNTAnata.json', 'var_call_ZTdot18lDnDpMr5KZpcZAXhb': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_vhYBsub8GGDs4cUovNNW9aLD': {'next': 'need_query_clinical_with_patient_description_like'}, 'var_call_RSUaCGLkHddl7kdpmS8IGwA4': 'file_storage/call_RSUaCGLkHddl7kdpmS8IGwA4.json', 'var_call_yomAYiIuf1OxhRIibtDRbQBZ': {'ct_shape': [8, 2], 'ct_columns': ['False', 'True'], 'ct_index_len': 8}, 'var_call_5ZQiPDz0ZuDEhuD6S64SgLY8': {'ct_row_shape': [5, 2], 'col_keep_type': "<class 'pandas.core.series.Series'>", 'col_keep_index': ['False', 'True'], 'col_keep_values': [1, 1]}}

exec(code, env_args)
