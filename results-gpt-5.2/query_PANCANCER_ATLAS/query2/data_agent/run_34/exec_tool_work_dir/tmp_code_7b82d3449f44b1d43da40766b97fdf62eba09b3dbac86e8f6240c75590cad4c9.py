code = """import json, re, pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

clin = load_records(var_call_ODlhBHElDrDSvZ91C54Xywos)
mut = load_records(var_call_WGv2m1JzUlp4mdjli6dHMOFk)

cdf = pd.DataFrame(clin)
mdf = pd.DataFrame(mut)

# extract TCGA barcode from patient_description text
pat = cdf['participantbarcode'].astype(str).str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
cdf['ParticipantBarcode'] = pat

# alive filter from description
cdf['is_alive'] = cdf['participantbarcode'].astype(str).str.contains(r'vital status\s*[:=]?\s*Alive', case=False, regex=True)

# keep BRCA only (note: hint says BRCA=Bladder urothelial carcinoma). infer BRCA cohort from description contains 'Bladder urothelial carcinoma'
cdf['is_brca'] = cdf['participantbarcode'].astype(str).str.contains(r'Bladder urothelial carcinoma', case=False, regex=False)

alive_brca = cdf[cdf['is_brca'] & cdf['is_alive'] & cdf['ParticipantBarcode'].notna()].copy()

mut_set = set(mdf['ParticipantBarcode'].astype(str))
alive_brca['has_CDH1_mut'] = alive_brca['ParticipantBarcode'].astype(str).isin(mut_set)

# compute per hist type
agg = alive_brca.groupby('hist_type').agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_mut=('has_CDH1_mut','sum')
).reset_index()
agg['pct_mut'] = (agg['n_mut'] / agg['n_alive'] * 100).round(2)

# only consider hist types with at least 5 alive patients to avoid tiny denominators
agg_f = agg[agg['n_alive']>=5].sort_values(['pct_mut','n_mut','n_alive'], ascending=[False, False, False]).head(3)

result = agg_f.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WGv2m1JzUlp4mdjli6dHMOFk': 'file_storage/call_WGv2m1JzUlp4mdjli6dHMOFk.json', 'var_call_IMN84FMWR7OWajjQCsktUtC7': [{'column_name': 'Patient_description'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}], 'var_call_m9G7pqzcXaMHhPeVtGSMIbM8': [], 'var_call_l77UpEGqZpPL0ij8hxqPQaa8': [], 'var_call_YY3bhht7x5wl2ZnkvDE14l0I': [], 'var_call_FrKFrLJ1YuzX0c6R30agon03': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_ODlhBHElDrDSvZ91C54Xywos': 'file_storage/call_ODlhBHElDrDSvZ91C54Xywos.json'}

exec(code, env_args)
