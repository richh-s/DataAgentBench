code = """import json, re, pandas as pd
from collections import defaultdict

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r') as f:
            return json.load(f)
    return maybe_path_or_records

clin = load_records(var_call_Xhv6BxMepgkRIQFjFeot4F3Q)
mut = load_records(var_call_wsom00buaGssm0Y87GXlZBhu)

# Parse participant barcode and alive status from Patient_description text
rows=[]
for r in clin:
    desc = r.get('participant') or ''
    m = re.search(r'patient\s+(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m:
        m = re.search(r'barcode\s+(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = m.group(1) if m else None
    alive = None
    if re.search(r'vital status\s*(?:is|=)?\s*Alive', desc, flags=re.IGNORECASE):
        alive = True
    elif re.search(r'vital status\s*(?:is|=)?\s*Dead', desc, flags=re.IGNORECASE):
        alive = False
    rows.append({'ParticipantBarcode': barcode, 'histological_type': r.get('histological_type'), 'alive': alive})

clin_df = pd.DataFrame(rows)
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])
clin_df = clin_df[clin_df['alive'] == True]

mut_df = pd.DataFrame(mut)
mut_df['mut_cnt'] = pd.to_numeric(mut_df['mut_cnt'], errors='coerce').fillna(0).astype(int)
mut_df['has_cdh1_mut'] = mut_df['mut_cnt'] > 0
mut_df = mut_df[['participant','has_cdh1_mut']].rename(columns={'participant':'ParticipantBarcode'})

df = clin_df.merge(mut_df, on='ParticipantBarcode', how='left')
df['has_cdh1_mut'] = df['has_cdh1_mut'].fillna(False)

# compute per histological type
agg = df.groupby('histological_type', dropna=False).agg(
    alive_n=('ParticipantBarcode','nunique'),
    mutated_n=('has_cdh1_mut','sum')
).reset_index()
agg['pct_cdh1_mut'] = (agg['mutated_n'] / agg['alive_n'] * 100).round(2)

# require at least 10 alive patients to avoid tiny denominators
agg_f = agg[agg['alive_n'] >= 10].sort_values(['pct_cdh1_mut','mutated_n','alive_n'], ascending=False)

top3 = agg_f.head(3)
result = top3.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DfRhYr1x8xqga6GSuLgdE2UM': ['clinical_info'], 'var_call_bpVf7muqQnZ0QlijAaFpcPwJ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_wsom00buaGssm0Y87GXlZBhu': 'file_storage/call_wsom00buaGssm0Y87GXlZBhu.json', 'var_call_WZnGLyrdlDyOMVI3c8L1K9Wr': [{'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_1te3WnqRyNlnG0izUx3y4SAn': [], 'var_call_UOWOBlKl3XlEhvgQP0go0esb': [], 'var_call_go4RYhrv0csBPBICzjx0FORC': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}], 'var_call_PJvmAW1a3NXmmgdM72PsY43f': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_Xhv6BxMepgkRIQFjFeot4F3Q': 'file_storage/call_Xhv6BxMepgkRIQFjFeot4F3Q.json'}

exec(code, env_args)
