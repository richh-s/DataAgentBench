code = """import json, re, pandas as pd

# Load full mutation data from file
path = var_call_qryqKFWADmfytCmPioY5fWHy
with open(path, 'r') as f:
    mut_records = json.load(f)
mut_df = pd.DataFrame(mut_records)

# Extract unique barcodes with CDH1 mutation
mut_barcodes = set(mut_df['ParticipantBarcode'].unique())

# Load full clinical data
path_clin = var_call_GsyXVtw4RAuAdBnT5lmOus9d
with open(path_clin, 'r') as f:
    clin_records = json.load(f)
clin_df = pd.DataFrame(clin_records)

# Parse patient barcode and vital status from Patient_description
barcode_pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}')

barcodes = []
vital_statuses = []
for desc in clin_df['Patient_description']:
    m = barcode_pattern.search(desc)
    barcodes.append(m.group(0) if m else None)
    # vital status appears like 'vital status: Alive.' or 'vital status = Dead.' etc.
    vs = None
    m2 = re.search(r'vital status[:=]\s*(Alive|Dead)', desc, re.IGNORECASE)
    if m2:
        vs = m2.group(1).capitalize()
    vital_statuses.append(vs)

clin_df['ParticipantBarcode'] = barcodes
clin_df['vital_status'] = vital_statuses

# Filter to BRCA patients: diagnoses or histological pattern mentioning 'breast' or 'BRCA'
# Here we approximate by looking for 'breast' in histological_type or diagnosis text
is_breast = clin_df['histological_type'].str.contains('breast', case=False, na=False) | \
            clin_df['Patient_description'].str.contains('Breast', case=False, na=False)

brca_df = clin_df[is_breast].copy()

# Keep only those with known vital status Alive
brca_alive = brca_df[brca_df['vital_status'] == 'Alive'].copy()

# Determine which of these patients have CDH1 mutation
brca_alive['has_CDH1_mut'] = brca_alive['ParticipantBarcode'].isin(mut_barcodes)

# For each histological_type, compute percentage with mutation
summary = brca_alive.groupby('histological_type').agg(
    total_patients=('ParticipantBarcode', 'nunique'),
    mutated_patients=('has_CDH1_mut', 'sum')
).reset_index()
summary['mutation_percentage'] = summary['mutated_patients'] / summary['total_patients'] * 100

# Get top 3 histological types by mutation_percentage (breaking ties by total_patients desc)
summary_sorted = summary.sort_values(['mutation_percentage', 'total_patients'], ascending=[False, False]).head(3)

result = summary_sorted.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_qryqKFWADmfytCmPioY5fWHy': 'file_storage/call_qryqKFWADmfytCmPioY5fWHy.json', 'var_call_Ga7p2kcfP5g3FVC8bZtc3cJz': ['clinical_info'], 'var_call_CkQueVyhbZgNTJGgZkA4lIlz': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_GsyXVtw4RAuAdBnT5lmOus9d': 'file_storage/call_GsyXVtw4RAuAdBnT5lmOus9d.json'}

exec(code, env_args)
