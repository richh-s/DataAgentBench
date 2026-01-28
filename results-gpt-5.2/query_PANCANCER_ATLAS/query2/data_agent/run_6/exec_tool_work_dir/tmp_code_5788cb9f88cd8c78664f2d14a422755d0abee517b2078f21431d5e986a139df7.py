code = """import json, re, pandas as pd

# Load alive BRCA (Breast site) clinical records
path_clin = var_call_L9DnDrNbnhummFnXyj1r8zYn
with open(path_clin, 'r') as f:
    clin = json.load(f)

def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

rows=[]
for r in clin:
    barcode = extract_barcode(r.get('participantbarcode') or r.get('ParticipantBarcode'))
    hist = r.get('histological_type')
    if barcode:
        rows.append({'ParticipantBarcode': barcode, 'histological_type': hist})

clin_df = pd.DataFrame(rows).dropna(subset=['ParticipantBarcode'])

# Load CDH1-mutated participants list
path_mut = var_call_JXMW5aDOgO3Cp7YJvooVnhRy
with open(path_mut, 'r') as f:
    muts = json.load(f)
mut_set = set([d['ParticipantBarcode'] for d in muts if 'ParticipantBarcode' in d])

clin_df['cdh1_mut'] = clin_df['ParticipantBarcode'].isin(mut_set)

g = clin_df.groupby('histological_type', dropna=False).agg(total=('ParticipantBarcode','nunique'), mutated=('cdh1_mut','sum'))
g['pct'] = (g['mutated'] / g['total'] * 100).round(2)

g = g.sort_values(['pct','mutated','total'], ascending=[False, False, False]).head(3).reset_index()
result = g.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JXMW5aDOgO3Cp7YJvooVnhRy': 'file_storage/call_JXMW5aDOgO3Cp7YJvooVnhRy.json', 'var_call_eRLMxz8WHooJAcgAORsYNxlI': ['clinical_info'], 'var_call_RkF5CZKkH0DndFAeDCXlpc61': [{'column_name': 'Patient_description'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_ZZxfJbep5yaFwoZOkDz9qibV': [], 'var_call_sKtc26W1ko4LM3w5JqYI6szj': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_A5JYgoPXtO8kO6grFaeZnvk3': [{'column_name': 'icd_o_3_site'}, {'column_name': 'tissue_source_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_5mt5uvdWJbP4LCVyn7EXoHOm': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_y3fHcIuCkA5olMkj9413VNBu': [], 'var_call_hpkPCQuaOkLfUw4Psduw8SBO': [{'person_neoplasm_cancer_status': 'TUMOR FREE', 'n': '873'}, {'person_neoplasm_cancer_status': 'None', 'n': '103'}, {'person_neoplasm_cancer_status': 'WITH TUMOR', 'n': '91'}, {'person_neoplasm_cancer_status': '[Unknown]', 'n': '20'}], 'var_call_FQToFONRu2ZBax8421aBMtjj': [], 'var_call_DiLHG6rI86CWvupdgvgR3v9p': [{'column_name': 'days_to_death'}, {'column_name': 'patient_death_reason'}], 'var_call_HaabX7O0sK5No1AyDRPtJluh': [{'tumor_tissue_site': 'Breast', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'days_to_death': '[Not Applicable]', 'n': '810'}, {'tumor_tissue_site': 'Kidney', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'days_to_death': '[Not Applicable]', 'n': '548'}, {'tumor_tissue_site': 'Lung', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'days_to_death': '[Not Applicable]', 'n': '474'}, {'tumor_tissue_site': 'Thyroid', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'days_to_death': '[Not Applicable]', 'n': '408'}, {'tumor_tissue_site': 'Endometrial', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'days_to_death': '[Not Applicable]', 'n': '385'}], 'var_call_L9DnDrNbnhummFnXyj1r8zYn': 'file_storage/call_L9DnDrNbnhummFnXyj1r8zYn.json'}

exec(code, env_args)
