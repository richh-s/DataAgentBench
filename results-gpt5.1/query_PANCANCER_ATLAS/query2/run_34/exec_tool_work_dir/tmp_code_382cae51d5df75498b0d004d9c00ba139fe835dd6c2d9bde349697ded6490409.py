code = """import json, pandas as pd
from pathlib import Path

# Load full clinical and CDH1 mutation data
clinical_path = var_call_RVIsjaVTYCmanF5cvkiecLA6
with open(clinical_path, 'r') as f:
    clinical = json.load(f)

cdh1_path = var_call_kCwe08jiAh3Bg2RBE71KrPgi
with open(cdh1_path, 'r') as f:
    cdh1 = json.load(f)

clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(cdh1).drop_duplicates(subset=['ParticipantBarcode'])

# Extract barcode and vital status from Patient_description
def parse_desc(desc):
    # Example: "Patient TCGA-36-1576 ... Vital status: Alive."
    barcode = None
    status = None
    parts = desc.split(' ')
    for p in parts:
        if p.startswith('TCGA-'):
            barcode = p.strip(',').strip()
            break
    low = desc.lower()
    if 'vital status: alive' in low:
        status = 'Alive'
    elif 'vital status: dead' in low:
        status = 'Dead'
    return barcode, status

clin_df['barcode'], clin_df['vital_status'] = zip(*clin_df['Patient_description'].map(parse_desc))

# Keep BRCA using ICD-O-3 site code for breast (C50.x)
clin_df['is_BRCA'] = clin_df['icd_o_3_site'].fillna('').str.startswith('C50')
brca_df = clin_df[clin_df['is_BRCA'] & (clin_df['vital_status'] == 'Alive')].copy()

# Merge with mutation data to flag CDH1 mutation
merged = brca_df.merge(mut_df, left_on='barcode', right_on='ParticipantBarcode', how='left', indicator=True)
merged['cdh1_mutated'] = merged['_merge'] == 'both'

# For each histological_type, compute percentage mutated among alive BRCA patients
summary = merged.groupby('histological_type').agg(
    n_total=('barcode', 'nunique'),
    n_mut=('cdh1_mutated', 'sum')
).reset_index()
summary['pct_mutated'] = summary['n_mut'] / summary['n_total'] * 100

# Filter to histological types with at least, say, 5 alive BRCA patients to avoid tiny groups
summary = summary[summary['n_total'] >= 5]

top3 = summary.sort_values('pct_mutated', ascending=False).head(3)

result = top3[['histological_type', 'pct_mutated', 'n_mut', 'n_total']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kCwe08jiAh3Bg2RBE71KrPgi': 'file_storage/call_kCwe08jiAh3Bg2RBE71KrPgi.json', 'var_call_xQXRTh7zHSoIZ4sf3qifvRrj': ['clinical_info'], 'var_call_ZE6863r6OBqCEf2spS16hCYF': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_RVIsjaVTYCmanF5cvkiecLA6': 'file_storage/call_RVIsjaVTYCmanF5cvkiecLA6.json'}

exec(code, env_args)
