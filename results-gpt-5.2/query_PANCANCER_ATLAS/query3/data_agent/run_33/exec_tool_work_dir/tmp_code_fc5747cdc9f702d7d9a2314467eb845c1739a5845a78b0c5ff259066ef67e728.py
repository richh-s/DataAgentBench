code = """import json, re, pandas as pd

path = var_call_1bq9qDvHTXYHPiYHQVWLs3Oo
with open(path,'r') as f:
    clin = json.load(f)
df_clin = pd.DataFrame(clin)

df_clin['ParticipantBarcode'] = df_clin['participantbarcode'].astype(str).str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)

def extract_cancer(s):
    if not isinstance(s,str):
        return None
    m = re.search(r'In the ([A-Za-z0-9 \-]+?) dataset', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'study of ([A-Za-z0-9 \-]+?)\.', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

df_clin['dataset_name'] = df_clin['participantbarcode'].apply(extract_cancer)

# filter BRCA cohort = breast invasive carcinoma dataset
mask_brca = df_clin['dataset_name'].str.contains('Breast', case=False, na=False)
mask_female = df_clin['participantbarcode'].str.contains('FEMALE', na=False)
df_clin_brca = df_clin[mask_brca & mask_female & df_clin['histological_type'].notna() & df_clin['ParticipantBarcode'].notna()].copy()

# mutations
mpath = var_call_zPjEcxfDTuGtux5VAvy8tUY4
with open(mpath,'r') as f:
    muts = json.load(f)
df_mut = pd.DataFrame(muts)
mut_patients = set(df_mut['ParticipantBarcode'].dropna().unique())

df_clin_brca['CDH1_mut'] = df_clin_brca['ParticipantBarcode'].isin(mut_patients)

ct = pd.crosstab(df_clin_brca['histological_type'], df_clin_brca['CDH1_mut'])
# rename cols
ct = ct.rename(columns={False:'WT', True:'MUT'})
for c in ['WT','MUT']:
    if c not in ct.columns:
        ct[c]=0
ct = ct[['WT','MUT']]

# filter marginal totals >10
ct_f = ct[ct.sum(axis=1) > 10]

obs = ct_f.to_numpy(dtype=float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ col_tot / grand
chi2 = float(((obs-exp)**2/exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

out = {
    'chi_square': chi2,
    'dof': dof,
    'grand_total': int(grand),
    'categories_used': int(obs.shape[0]),
    'contingency_table': (
        ct_f.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
    )
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zPjEcxfDTuGtux5VAvy8tUY4': 'file_storage/call_zPjEcxfDTuGtux5VAvy8tUY4.json', 'var_call_k8HwBalFqgayAG9YnAvAOFlv': ['clinical_info'], 'var_call_V1fUTuA8ocQcGo9c5Hyxh3QI': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_qJ2nWXR4EzjrJ98DGo4F0CW8': [], 'var_call_2K5cPQ70H18PIc3apAuDle0z': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'patient_id': '1953', 'diagnosis': 'None', 'icd_10': 'C56.9', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'patient_id': '1576', 'diagnosis': 'None', 'icd_10': 'C56.9', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'patient_id': '2408', 'diagnosis': 'None', 'icd_10': 'C56.9', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'patient_id': '2427', 'diagnosis': 'None', 'icd_10': 'C56.9', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'patient_id': '0933', 'diagnosis': 'None', 'icd_10': 'C56.9', 'tumor_tissue_site': 'Ovary'}], 'var_call_6kxwe0T5EYveoWDjca5g32sl': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'n': '777'}, {'histological_type': 'Serous Cystadenocarcinoma', 'n': '584'}, {'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'histological_type': 'Kidney Clear Cell Renal Carcinoma', 'n': '518'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma', 'n': '512'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type', 'n': '480'}, {'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'n': '470'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'n': '409'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma', 'n': '401'}, {'histological_type': 'Colon Adenocarcinoma', 'n': '378'}], 'var_call_1bq9qDvHTXYHPiYHQVWLs3Oo': 'file_storage/call_1bq9qDvHTXYHPiYHQVWLs3Oo.json'}

exec(code, env_args)
