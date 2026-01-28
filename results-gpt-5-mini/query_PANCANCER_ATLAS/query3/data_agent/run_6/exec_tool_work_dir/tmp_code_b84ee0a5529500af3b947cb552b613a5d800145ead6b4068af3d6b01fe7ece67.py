code = """import pandas as pd
import json
import re
import numpy as np

# Load data from storage-provided file paths
clinical_path = var_call_VJG2iCWQfZt8H5NtOLSdoX0W
mut_path = var_call_HFxYtNV89LYasiyD2KdL3Yyg

clinical = pd.read_json(clinical_path)
mut = pd.read_json(mut_path)

# Extract TCGA barcode from Patient_description
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'TCGA[-][A-Za-z0-9-]+', text)
    if m:
        # take up to first whitespace or punctuation
        barcode = m.group(0)
        # strip trailing punctuation
        barcode = re.sub(r'[.,;:]$', '', barcode)
        return barcode
    return None

clinical['barcode'] = clinical['Patient_description'].apply(extract_barcode)
# Keep rows with barcode and histological_type known
clinical = clinical[clinical['barcode'].notna() & clinical['histological_type'].notna()]
# Keep unique patients (if duplicates, keep first)
clinical = clinical.drop_duplicates(subset=['barcode']).copy()

# Set of mutated patient barcodes from mutation table
mutated_set = set(mut['ParticipantBarcode'].dropna().unique())

# Determine mutation presence per patient
clinical['CDH1_mutated'] = clinical['barcode'].apply(lambda x: x in mutated_set)

# Build contingency table: histological_type vs mutation presence
ct = pd.crosstab(clinical['histological_type'], clinical['CDH1_mutated'])
# Ensure both columns exist (False, True)
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]

# Exclude histological types with marginal totals <= 10
ct['row_total'] = ct.sum(axis=1)
ct_filtered = ct[ct['row_total'] > 10].drop(columns=['row_total'])

# If no categories remain, return message
if ct_filtered.shape[0] < 2:
    result = {"error": "Not enough histological categories with total > 10 to compute chi-square after filtering."}
else:
    obs = ct_filtered.values.astype(float)
    row_totals = obs.sum(axis=1).reshape(-1,1)
    col_totals = obs.sum(axis=0).reshape(1,-1)
    grand_total = obs.sum()
    expected = row_totals.dot(col_totals) / grand_total
    # Avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        chi2 = np.nansum((obs - expected)**2 / expected)
    # Prepare output
    # Convert observed to dict
    obs_dict = {}
    for idx, row in enumerate(ct_filtered.index):
        obs_dict[row] = {"Not_Mutated": int(obs[idx,0]), "Mutated": int(obs[idx,1]), "Row_Total": int(obs[idx].sum())}
    col_totals_list = {"Not_Mutated": int(col_totals[0,0]), "Mutated": int(col_totals[0,1]), "Grand_Total": int(grand_total)}
    result = {"chi2": float(chi2), "observed_by_histology": obs_dict, "column_totals": col_totals_list}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_66FQ3X8I18ech3D2reUjRPhU': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_ALFwwCUHSRMb52LoVoyfmAe6': [], 'var_call_AfruguUVTMgF3wc4Ch5gcjBG': [], 'var_call_eUsldShlvtnOeezxQrKnkSbu': 'file_storage/call_eUsldShlvtnOeezxQrKnkSbu.json', 'var_call_dMaeD4wkq2kaM19KCWRwr1ql': 'file_storage/call_dMaeD4wkq2kaM19KCWRwr1ql.json', 'var_call_VJG2iCWQfZt8H5NtOLSdoX0W': 'file_storage/call_VJG2iCWQfZt8H5NtOLSdoX0W.json', 'var_call_HFxYtNV89LYasiyD2KdL3Yyg': 'file_storage/call_HFxYtNV89LYasiyD2KdL3Yyg.json'}

exec(code, env_args)
