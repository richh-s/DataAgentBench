code = """import json, re, pandas as pd

# Load clinical breast cohort
path = var_call_NgndiW6YhK1Xdf63LTz5lj6t
with open(path, 'r') as f:
    clin = json.load(f)

df = pd.DataFrame(clin)

# Extract TCGA barcode from Patient_description
def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

df['ParticipantBarcode'] = df['Patient_description'].map(extract_barcode)

# Alive: days_to_death is [Not Applicable] or None/empty; treat numeric as dead
alive_mask = df['days_to_death'].isna() | (df['days_to_death'].astype(str).str.contains('Not Applicable', na=False))
# Some rows could have days_to_death='None' string
alive_mask = alive_mask | (df['days_to_death'].astype(str).str.lower().isin(['none','nan','']))

alive = df[alive_mask & df['ParticipantBarcode'].notna()].copy()

# CDH1 mutated participants
mut_path = var_call_EHyaCi9XtpDEpmrWT6dP41Ok
with open(mut_path, 'r') as f:
    mut = json.load(f)
mut_set = set([r['ParticipantBarcode'] for r in mut if r.get('ParticipantBarcode')])

alive['cdh1_mut'] = alive['ParticipantBarcode'].isin(mut_set)

# Group by histological_type
alive['histological_type'] = alive['histological_type'].fillna('Unknown')

g = alive.groupby('histological_type').agg(
    alive_n=('ParticipantBarcode','nunique'),
    cdh1_mut_n=('cdh1_mut','sum')
).reset_index()

g['pct_cdh1_mut'] = (g['cdh1_mut_n'] / g['alive_n'] * 100).round(2)

# Keep histology types with at least 5 alive patients to avoid tiny denominators
# (not specified; but keep all; still sort by pct desc then alive_n desc)
res = g.sort_values(['pct_cdh1_mut','alive_n'], ascending=[False, False]).head(3)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EHyaCi9XtpDEpmrWT6dP41Ok': 'file_storage/call_EHyaCi9XtpDEpmrWT6dP41Ok.json', 'var_call_5rUyIlVlFp6XVa3WR1pAKq8A': [], 'var_call_mCaaD5pKHwpaTa8A6gWgzbC5': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}], 'var_call_Mu5Z3eWoJxa1W660fIfYy38R': [], 'var_call_USCZKkZ8p3V1tYxa6pfmHTK9': [{'column_name': 'days_to_death'}, {'column_name': 'patient_death_reason'}], 'var_call_30zFcGhMHZjuaJauWTz20rCS': [{'column_name': 'days_to_last_followup'}], 'var_call_BIS0gEZ0R3fLv9YZCSgGS9aL': [{'column_name': 'icd_o_3_histology'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}], 'var_call_dcyvbqDwHaLy0ofmY3Vh00IZ': [], 'var_call_PAl43BNbtjXZ2PoKLHzXWSwR': [], 'var_call_NBjn1bf1IzSjObNGLcaagWdr': [{'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}], 'var_call_VzLgfqzUFMb3VXPdNgomQoN6': [], 'var_call_W2JUcqbC5KFJpyHkTVgJCWmr': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_NgndiW6YhK1Xdf63LTz5lj6t': 'file_storage/call_NgndiW6YhK1Xdf63LTz5lj6t.json'}

exec(code, env_args)
