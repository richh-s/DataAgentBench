code = """import json, pandas as pd, re

# load breast clinical rows
path = var_call_wnjRkgFPd6SqACtoQizywwtq
with open(path, 'r') as f:
    clin = json.load(f)

df = pd.DataFrame(clin)
# participantbarcode key lowercased by driver
pb_col = 'participantbarcode' if 'participantbarcode' in df.columns else 'ParticipantBarcode'

def extract_tcga_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

df['ParticipantBarcode'] = df[pb_col].map(extract_tcga_barcode)
# alive filter based on text containing 'vital status' and 'Alive'
df['is_alive'] = df[pb_col].astype(str).str.contains(r'vital status\s*(?:is|=|recorded as)?\s*Alive', case=False, regex=True)

df_alive = df[df['is_alive']].copy()
# keep needed cols
if 'histological_type' not in df_alive.columns:
    df_alive['histological_type'] = None

# load CDH1 mutated participants list
mut_path = var_call_kTsk1D61kisMlumqD8709XPh
with open(mut_path, 'r') as f:
    cdh1 = json.load(f)
mut_set = set([r['ParticipantBarcode'] for r in cdh1 if r.get('ParticipantBarcode')])

df_alive['has_CDH1_mut'] = df_alive['ParticipantBarcode'].isin(mut_set)

# compute percentage by histological_type
agg = (df_alive.groupby('histological_type', dropna=False)
       .agg(total_alive=('ParticipantBarcode','nunique'),
            mutated_alive=('has_CDH1_mut','sum'))
       .reset_index())
agg['pct_mutated'] = (agg['mutated_alive'] / agg['total_alive'] * 100).round(2)

# remove missing/empty hist types
agg = agg[agg['histological_type'].notna() & (agg['histological_type'].astype(str).str.strip()!='')]

# to avoid tiny denominators, still keep all; sort by pct then mutated count then total
agg = agg.sort_values(['pct_mutated','mutated_alive','total_alive'], ascending=[False,False,False]).head(3)

result = agg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kTsk1D61kisMlumqD8709XPh': 'file_storage/call_kTsk1D61kisMlumqD8709XPh.json', 'var_call_NxIFIM6gILDXCvpJXirgBKRH': ['clinical_info'], 'var_call_VxQn1ONoo3Qg0Kd6puJnLBaZ': [], 'var_call_BzjgrGp0PT6mA8vC99veV1ZM': [{'column_name': 'days_to_death'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'patient_death_reason'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}], 'var_call_NPWM2Qg0KyWkMCkpjDi4gv9g': [{'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}], 'var_call_P2S2EpeGbJPdDZIHFwPUDtuQ': [{'column_name': 'Patient_description'}], 'var_call_KUYGmbMSRhleghFCU4lvWFzv': [], 'var_call_1qDv4pn7LcXXa7gILZzR118q': [{'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'family_history_of_cancer'}], 'var_call_rYa463B4hsMdZ873NFeQ52j2': [], 'var_call_886mXefu2vjNgmDlYxTCUJTf': [], 'var_call_sh5JGoBO0y1bbbZ8gRPCexLl': [{'cancer': 'Breast', 'n': '1087'}, {'cancer': 'Lung', 'n': '1004'}, {'cancer': 'Kidney', 'n': '869'}, {'cancer': 'Brain', 'n': '590'}, {'cancer': 'Ovary', 'n': '579'}, {'cancer': 'Head and Neck', 'n': '560'}, {'cancer': 'Endometrial', 'n': '530'}, {'cancer': 'Central nervous system', 'n': '513'}, {'cancer': 'Thyroid', 'n': '503'}, {'cancer': 'Prostate', 'n': '495'}, {'cancer': 'Colon', 'n': '442'}, {'cancer': 'Stomach', 'n': '440'}, {'cancer': 'Bladder', 'n': '412'}, {'cancer': 'Liver', 'n': '374'}, {'cancer': 'Cervical', 'n': '306'}, {'cancer': 'Extremities', 'n': '193'}, {'cancer': 'Pancreas', 'n': '184'}, {'cancer': 'Esophagus', 'n': '183'}, {'cancer': 'Trunk', 'n': '169'}, {'cancer': 'Rectum', 'n': '156'}], 'var_call_wnjRkgFPd6SqACtoQizywwtq': 'file_storage/call_wnjRkgFPd6SqACtoQizywwtq.json'}

exec(code, env_args)
