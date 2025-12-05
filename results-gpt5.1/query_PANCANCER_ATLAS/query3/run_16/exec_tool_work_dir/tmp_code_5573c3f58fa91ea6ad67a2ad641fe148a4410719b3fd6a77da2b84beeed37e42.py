code = """import json, re, pandas as pd
from collections import Counter

# Load mutation data
with open(var_call_wEhXtJiV5EvFUosgN9qXmthK, 'r') as f:
    mut_records = json.load(f)

mut_df = pd.DataFrame(mut_records)
# CDH1 mutated patients (reliable = FILTER PASS already)
mut_patients = set(mut_df['ParticipantBarcode'].unique())

# Load clinical data
with open(var_call_fP414bxuGQy44Uxh8D9aES00, 'r') as f:
    clin_records = json.load(f)

clin_df = pd.DataFrame(clin_records)

# Extract barcode from Patient_description using regex TCGA-*-*
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(lambda x: barcode_pattern.search(x).group(1) if isinstance(x,str) and barcode_pattern.search(x) else None)

# Keep only rows with known barcode
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# Focus on females only (Patient_description contains 'FEMALE')
clin_df = clin_df[clin_df['Patient_description'].str.contains('FEMALE')]

# Deduplicate per patient by keeping first record
clin_df = clin_df.drop_duplicates(subset=['ParticipantBarcode'])

# Create mutation presence column
clin_df['CDH1_mutated'] = clin_df['ParticipantBarcode'].isin(mut_patients)

# Contingency table histological_type vs mutation
cont = pd.crosstab(clin_df['histological_type'], clin_df['CDH1_mutated'])

# Exclude categories with marginal totals <=10 (row or column)
row_totals = cont.sum(axis=1)
col_totals = cont.sum(axis=0)
cont_filtered = cont[(row_totals > 10)]
# For columns, mutation True/False, require both >10
cont_filtered = cont_filtered.loc[:, col_totals > 10]

# If after filtering table is too small, handle
if cont_filtered.size == 0 or cont_filtered.shape[0] < 2 or cont_filtered.shape[1] < 2:
    result = {'error': 'Contingency table too small after filtering', 'table': cont.to_dict()}
else:
    # Compute chi-square manually
    grand_total = cont_filtered.values.sum()
    row_tot = cont_filtered.sum(axis=1).values.reshape(-1,1)
    col_tot = cont_filtered.sum(axis=0).values.reshape(1,-1)
    expected = row_tot @ col_tot / grand_total
    observed = cont_filtered.values
    chi2 = ((observed - expected)**2 / expected).sum()
    result = {
        'chi_square_statistic': float(chi2),
        'contingency_table': cont_filtered.to_dict(),
        'grand_total': int(grand_total)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wEhXtJiV5EvFUosgN9qXmthK': 'file_storage/call_wEhXtJiV5EvFUosgN9qXmthK.json', 'var_call_52qDSN6FtrrvFvOkJKuPeiEI': ['clinical_info'], 'var_call_2mKfbD2MpFXaB2aQ4aLlAvEW': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_fP414bxuGQy44Uxh8D9aES00': 'file_storage/call_fP414bxuGQy44Uxh8D9aES00.json'}

exec(code, env_args)
