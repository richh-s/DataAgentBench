code = """import pandas as pd
import re
import json
import numpy as np

# Load the large JSON results from storage file paths
clinical_path = var_call_o6OmW8GjAd0EppjqhtyzEyGX
rna_path = var_call_99Kz1VPaSVZiFrrSxfYBrHYW

clin = pd.read_json(clinical_path)
rna = pd.read_json(rna_path)

# Extract TCGA barcode from Patient_description
# Pattern: TCGA-XX-YYYY (YY may be letters/digits, YYYY typically 4 chars)
clin['barcode'] = clin['Patient_description'].str.extract(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,4})', expand=False)

# Filter out rows without barcode
clin = clin[clin['barcode'].notna()].copy()

# Filter histological_type that are not entirely enclosed in square brackets
# Drop rows where histological_type matches ^\[.*\]$
clin = clin[clin['histological_type'].notna()].copy()
mask_brackets = clin['histological_type'].str.match(r'^\[.*\]$')
clin = clin[~mask_brackets].copy()

# Prepare RNA expression: ensure normalized_count numeric and valid
rna['normalized_count'] = pd.to_numeric(rna['normalized_count'], errors='coerce')
rna = rna[rna['normalized_count'].notna()].copy()

# Merge on barcode / ParticipantBarcode
merged = pd.merge(rna, clin, left_on='ParticipantBarcode', right_on='barcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_igf2'] = np.log10(merged['normalized_count'] + 1)

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type', dropna=True)['log10_igf2'].mean().reset_index()

# Format results with at least four decimal places
result_dict = {}
for _, row in grouped.iterrows():
    hist = row['histological_type']
    val = float(row['log10_igf2'])
    # Format to 4 decimal places (but keep as float)
    result_dict[hist] = float(f"{val:.4f}")

# Sort result_dict by histology name for consistent output
result_sorted = {k: result_dict[k] for k in sorted(result_dict.keys())}

print('__RESULT__:')
print(json.dumps(result_sorted))"""

env_args = {'var_call_CmdF26izdFhoOhzlbMH9qF8r': ['clinical_info'], 'var_call_7rKrfalq5BKxWsQdC8zRE5Fj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0y5pz4NbnctJNCd4OPYBvkdU': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_99Kz1VPaSVZiFrrSxfYBrHYW': 'file_storage/call_99Kz1VPaSVZiFrrSxfYBrHYW.json', 'var_call_oQzEZLXCLMn5O11EHb3gWCoj': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'None'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_aPyJ6iH0bQlbkIEDtW5eRlYM': 'file_storage/call_aPyJ6iH0bQlbkIEDtW5eRlYM.json', 'var_call_o6OmW8GjAd0EppjqhtyzEyGX': 'file_storage/call_o6OmW8GjAd0EppjqhtyzEyGX.json'}

exec(code, env_args)
