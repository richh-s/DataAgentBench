code = """import json, re, pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r') as f:
            return json.load(f)
    return x

clinical = load_result(var_call_lwCqpw0f0d7OKmNaGptn4Qw7)
cdh1 = load_result(var_call_P5OqYgY9aHsD5B0VxWTUNlZp)

cdf = pd.DataFrame(clinical)
mdf = pd.DataFrame(cdh1)

# extract barcode and alive status from Patient_description
pat = cdf['Patient_description'].fillna('')
barcode = pat.str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
alive = pat.str.contains(r'vital status\s*(?:is|=|recorded as)\s*Alive', case=False, regex=True)

cdf = cdf.assign(ParticipantBarcode=barcode, alive=alive)
# Keep alive BRCA (breast) patients with non-null histological_type and barcode
alive_df = cdf[(cdf['alive']) & (cdf['ParticipantBarcode'].notna())].copy()

# mutation flag
cdh1_set = set(mdf['ParticipantBarcode'].dropna().unique().tolist())
alive_df['cdh1_mut'] = alive_df['ParticipantBarcode'].isin(cdh1_set)

# compute per histological_type
alive_df['histological_type'] = alive_df['histological_type'].fillna('Unknown')
agg = alive_df.groupby('histological_type').agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_cdh1=('cdh1_mut','sum')
).reset_index()
agg['pct_cdh1'] = (agg['n_cdh1'] / agg['n_alive'] * 100).round(2)

# filter hist types with at least 10 alive patients to avoid tiny denominators
agg_f = agg[agg['n_alive']>=10].sort_values(['pct_cdh1','n_cdh1','n_alive'], ascending=[False,False,False]).head(3)

result = agg_f.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_P5OqYgY9aHsD5B0VxWTUNlZp': 'file_storage/call_P5OqYgY9aHsD5B0VxWTUNlZp.json', 'var_call_VoWW2WXyrbIDpW1MYW6p2ukc': ['clinical_info'], 'var_call_wrTGzbEC8LTF1AT0wzRMoKpp': [], 'var_call_Vtkt2KJyiiGz3KvYBFxpVpOx': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}], 'var_call_2UxISofPzhgQ9HITYYfZJ9Kq': [], 'var_call_FSm1ZvrRtpLvkSehWiiZwSDR': [{'column_name': 'days_to_death'}, {'column_name': 'patient_death_reason'}], 'var_call_YhQ75d93Hm82lAtwv9T0YAlc': [], 'var_call_88trJdec1TTvekSp6VLMX6w2': [], 'var_call_YCqqbndrEsGJKjX0dozcGzxX': [], 'var_call_j8yIKQfOmbto9OAkFUXf6ru8': [], 'var_call_eigiPHD6aWxAbbZVIlaPdbYN': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}], 'var_call_pQISTdj0q7ZJqJS5ZtXCTAJ2': [{'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}], 'var_call_2QdyIAMMPH0JNEvrdwZ8qf1E': [{'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Cervical'}], 'var_call_lwCqpw0f0d7OKmNaGptn4Qw7': 'file_storage/call_lwCqpw0f0d7OKmNaGptn4Qw7.json'}

exec(code, env_args)
