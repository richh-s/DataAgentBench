code = """import json, re, pandas as pd

def extract_acronym(desc):
    if desc is None:
        return None
    patterns = [
        r"In the (.*?) dataset, patient",
        r"enrolled in the study of (.*?). Vital status",
        r"diagnosed with (.*?). Current vital status",
        r"diagnosed with (.*?). Vital status recorded",
        r"belongs to the (.*?) cohort",
        r"subject with (.*?). Their current vital status",
        r"case of (.*?), documented",
        r"dataset, patient .*? diagnosed with (.*?)."
    ]
    name=None
    for pat in patterns:
        m=re.search(pat, desc)
        if m:
            name=m.group(1).strip()
            break
    if not name:
        return None
    mapping={
        'Breast invasive carcinoma':'BRCA',
        'Ovarian serous cystadenocarcinoma':'OV',
        'Glioblastoma multiforme':'GBM'
    }
    return mapping.get(name)

def extract_gender(desc):
    if desc is None:
        return None
    m=re.search(r"\b(MALE|FEMALE)\b", desc)
    return m.group(1).lower() if m else None

def extract_barcode(desc):
    if desc is None:
        return None
    m=re.search(r"\b(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})\b", desc)
    return m.group(1) if m else None

clin_path=var_call_RcuF78OXt7xaGKQyDa5YGICh
with open(clin_path,'r') as f:
    clin=json.load(f)
clin_df=pd.DataFrame(clin)
clin_df['participant_barcode']=clin_df['Patient_description'].map(extract_barcode)
clin_df['gender']=clin_df['Patient_description'].map(extract_gender)
clin_df['acronym']=clin_df['Patient_description'].map(extract_acronym)
clin_df=clin_df.dropna(subset=['participant_barcode','gender','acronym','histological_type'])
clin_df=clin_df[(clin_df['acronym']=='BRCA') & (clin_df['gender']=='female')]
clin_df=clin_df[['participant_barcode','histological_type']].drop_duplicates('participant_barcode')

mut_path=var_call_WBYSdoE7rAyWKiaXUl4rJueQ
with open(mut_path,'r') as f:
    mut=json.load(f)
mut_df=pd.DataFrame(mut)
mut_set=set(mut_df['participant_barcode'].dropna().unique())
clin_df['cdh1_mut']=clin_df['participant_barcode'].isin(mut_set)

ct=pd.crosstab(clin_df['histological_type'], clin_df['cdh1_mut'])
for col in [False, True]:
    if col not in ct.columns:
        ct[col]=0
ct=ct[[False, True]]
ct['row_total']=ct.sum(axis=1)
ct=ct[ct['row_total']>10].drop(columns=['row_total'])

# after row filtering, decide col filtering
col_totals=ct.sum(axis=0)
keep_cols=[c for c in ct.columns if col_totals[c]>10]
ct2=ct[keep_cols]

import numpy as np
obs=ct2.to_numpy(dtype=float)
if obs.size==0 or obs.shape[0]<2 or obs.shape[1]<2:
    result={'error':'Not enough data after filtering','n_patients_brca_female_known_hist':int(len(clin_df)),'row_categories_after_filter':int(obs.shape[0]) if obs.size else 0,'col_categories_after_filter':int(obs.shape[1]) if obs.size else 0,'col_totals':{str(k):int(v) for k,v in col_totals.items()},'hist_type_counts':clin_df['histological_type'].value_counts().head(20).to_dict()}
else:
    row_tot=obs.sum(axis=1,keepdims=True)
    col_tot=obs.sum(axis=0,keepdims=True)
    grand=obs.sum()
    exp=row_tot @ (col_tot/grand)
    chi2=float(((obs-exp)**2/exp).sum())
    df=int((obs.shape[0]-1)*(obs.shape[1]-1))
    result={
        'n_patients':int(len(clin_df)),
        'n_categories_kept':int(obs.shape[0]),
        'columns_kept':[str(c) for c in ct2.columns.tolist()],
        'grand_total_used':int(grand),
        'chi_square':chi2,
        'degrees_of_freedom':df,
        'contingency_table':ct2.reset_index().to_dict(orient='records')
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WBYSdoE7rAyWKiaXUl4rJueQ': 'file_storage/call_WBYSdoE7rAyWKiaXUl4rJueQ.json', 'var_call_W3eU78palg0byRI85upVwrdw': ['clinical_info'], 'var_call_wlZmqUDhB7hKeNTrVoeKHVSS': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_Qeh3Y9LlOA6uieVZ4OsC7TCJ': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_S5HX1HWH7lZMJYbIHVxYav9V': [], 'var_call_58CcEPWWKP0kLmdYOwIwMWaL': {'need': 'clinical_query_all_rows_with_patient_description_and_histological_type'}, 'var_call_RcuF78OXt7xaGKQyDa5YGICh': 'file_storage/call_RcuF78OXt7xaGKQyDa5YGICh.json'}

exec(code, env_args)
