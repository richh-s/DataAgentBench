code = """import re, json, pandas as pd, os

# Load full clinical data
path = var_call_fWv1sMNxnyjOztBnnRESsW6L
with open(path, 'r') as f:
    clinical = json.load(f)

# Extract barcode and gender and cancer type (BRCA) from Patient_description
records = []
for row in clinical:
    desc = row.get('Patient_description','') or ''
    hist = row.get('histological_type')
    if not hist:
        continue
    m = re.search(r'patient (TCGA-[A-Z0-9-]+)', desc)
    if not m:
        m = re.search(r'barcode (TCGA-[A-Z0-9-]+)', desc)
    if not m:
        continue
    barcode = m.group(1)
    gender = 'FEMALE' if ' FEMALE ' in desc or desc.strip().startswith('Patient') and 'FEMALE' in desc else ('MALE' if ' MALE ' in desc or 'MALE,' in desc else None)
    if gender != 'FEMALE':
        continue
    cancer = None
    m2 = re.search(r'diagnosed with ([A-Za-z ]+).', desc)
    if m2:
        cancer = m2.group(1)
    else:
        if 'breast' in desc.lower():
            cancer = 'Breast invasive carcinoma'
    if not cancer or 'breast' not in cancer.lower():
        continue
    records.append({'ParticipantBarcode': barcode, 'histological_type': hist})

clinical_df = pd.DataFrame(records).drop_duplicates()

# Load CDH1 mutations and keep reliable (FILTER='PASS')
path_mut = var_call_P8JaXXnGJ76IKN4AzH36QiYS
with open(path_mut, 'r') as f:
    muts = json.load(f)

mut_df = pd.DataFrame(muts)
mut_df = mut_df[mut_df['FILTER']=='PASS'].drop_duplicates(subset=['ParticipantBarcode'])
mut_df['CDH1_mut'] = 1

# Merge
merged = clinical_df.merge(mut_df[['ParticipantBarcode','CDH1_mut']], on='ParticipantBarcode', how='left')
merged['CDH1_mut'] = merged['CDH1_mut'].fillna(0).astype(int)

# Contingency table
ct = pd.crosstab(merged['histological_type'], merged['CDH1_mut'])
# Exclude categories with marginal totals <=10
ct = ct[ct.sum(axis=1) > 10]

# Compute chi-square
import numpy as np
observed = ct.values
row_tot = observed.sum(axis=1, keepdims=True)
col_tot = observed.sum(axis=0, keepdims=True)
grand = observed.sum()
expected = row_tot * col_tot / grand
chi2 = float(((observed - expected)**2 / expected).sum())

result = {
  'chi_square_statistic': chi2,
  'degrees_of_freedom': int((ct.shape[0]-1)*(ct.shape[1]-1)),
  'contingency_table': ct.reset_index().to_dict(orient='list')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_P8JaXXnGJ76IKN4AzH36QiYS': 'file_storage/call_P8JaXXnGJ76IKN4AzH36QiYS.json', 'var_call_qfgdBn4ItTT4F1CCAa8e1AB5': ['clinical_info'], 'var_call_OEyGywR5jpJEBw6q42zFRVxm': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_fWv1sMNxnyjOztBnnRESsW6L': 'file_storage/call_fWv1sMNxnyjOztBnnRESsW6L.json'}

exec(code, env_args)
