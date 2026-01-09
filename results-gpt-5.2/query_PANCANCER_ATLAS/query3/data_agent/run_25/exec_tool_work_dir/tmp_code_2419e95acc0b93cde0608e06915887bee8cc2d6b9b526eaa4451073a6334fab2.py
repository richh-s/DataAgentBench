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

print('__RESULT__:')
print(json.dumps({'ct_row_shape': ct_row.shape, 'col_keep_type': str(type(col_keep)), 'col_keep_index': [str(i) for i in col_keep.index], 'col_keep_values': col_keep.astype(int).tolist()}))"""

env_args = {'var_call_PqpLrorFd3BfHgtqY7qwFFPF': 'file_storage/call_PqpLrorFd3BfHgtqY7qwFFPF.json', 'var_call_fQbC0gKJszbQ3fBWkKhSoVe5': ['clinical_info'], 'var_call_Pip4ptun5TBx8ujfmNTAnata': 'file_storage/call_Pip4ptun5TBx8ujfmNTAnata.json', 'var_call_ZTdot18lDnDpMr5KZpcZAXhb': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_vhYBsub8GGDs4cUovNNW9aLD': {'next': 'need_query_clinical_with_patient_description_like'}, 'var_call_RSUaCGLkHddl7kdpmS8IGwA4': 'file_storage/call_RSUaCGLkHddl7kdpmS8IGwA4.json', 'var_call_yomAYiIuf1OxhRIibtDRbQBZ': {'ct_shape': [8, 2], 'ct_columns': ['False', 'True'], 'ct_index_len': 8}}

exec(code, env_args)
