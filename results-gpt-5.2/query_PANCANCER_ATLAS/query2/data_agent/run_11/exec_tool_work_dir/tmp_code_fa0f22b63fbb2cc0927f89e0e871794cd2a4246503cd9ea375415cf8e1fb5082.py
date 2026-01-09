code = """import json, re, pandas as pd

# Load alive BRCA (Breast site) clinical records
path_alive = var_call_JpSoB089WxMxYvG7Bg14600N
with open(path_alive, 'r') as f:
    alive_records = json.load(f)

df_alive = pd.DataFrame(alive_records)

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

df_alive['ParticipantBarcode'] = df_alive['Patient_description'].map(extract_barcode)

# Load CDH1 mutated participants (all cancers)
path_mut = var_call_cOVMzYBqOoYAWJGdGmPup4tI
with open(path_mut, 'r') as f:
    mut_records = json.load(f)
mut_set = set(r['ParticipantBarcode'] for r in mut_records if r.get('ParticipantBarcode'))

df_alive['has_CDH1_mut'] = df_alive['ParticipantBarcode'].isin(mut_set)

# Compute per histological_type percentages among alive
# Exclude missing histological_type or barcode
df = df_alive.dropna(subset=['ParticipantBarcode','histological_type']).copy()

grp = df.groupby('histological_type').agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_mut=('has_CDH1_mut','sum')
).reset_index()

# Percentage
grp['pct_mut'] = (grp['n_mut'] / grp['n_alive'] * 100).round(2)

# Filter to types with at least 5 alive cases to avoid tiny denominators? (not specified) -> don't filter.

top3 = grp.sort_values(['pct_mut','n_mut','n_alive'], ascending=[False, False, False]).head(3)

result = top3.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cOVMzYBqOoYAWJGdGmPup4tI': 'file_storage/call_cOVMzYBqOoYAWJGdGmPup4tI.json', 'var_call_KBlaKz6FqI7MJ0tudYg17f9Z': ['clinical_info'], 'var_call_ec4wUgsENKIISlhU0BKM8N4g': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_4Ie8pr49NBs8eI8EqP575oW1': [], 'var_call_tMRz6jmUKzlOOmXyK5GKn03o': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_thU77GYlY8LzciUEs6dS7YcP': [], 'var_call_uxAO3l9LLojJgBgOPBkaVZ4u': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'diagnosis': 'None', 'tumor_tissue_site': 'Ovary', 'icd_o_3_site': 'C56.9'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'diagnosis': 'None', 'tumor_tissue_site': 'Ovary', 'icd_o_3_site': 'C56.9'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'diagnosis': 'None', 'tumor_tissue_site': 'Ovary', 'icd_o_3_site': 'C56.9'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'diagnosis': 'None', 'tumor_tissue_site': 'Ovary', 'icd_o_3_site': 'C56.9'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'diagnosis': 'None', 'tumor_tissue_site': 'Ovary', 'icd_o_3_site': 'C56.9'}], 'var_call_X2s1SUhyKCYfJIIjBcIsCoGw': [], 'var_call_LdcBgR2spyl9if3WN9wc17a5': [{'n_total': '10761', 'n_alive': '3568'}], 'var_call_JpSoB089WxMxYvG7Bg14600N': 'file_storage/call_JpSoB089WxMxYvG7Bg14600N.json'}

exec(code, env_args)
