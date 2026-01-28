code = """import json
import pandas as pd
import re
import math

# Load previous tool results (file paths)
with open(var_call_hllnPay0oAiICqic78iKG5Jz, 'r') as f:
    clinical = json.load(f)
with open(var_call_UVUPK7amQst51vXaWgWbiQel, 'r') as f:
    igf2 = json.load(f)

clin_df = pd.DataFrame(clinical)
igf2_df = pd.DataFrame(igf2)

# Extract TCGA barcode from Patient_description
pattern = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(1) if m else None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Keep only rows with a barcode and non-null histological_type
clin_df = clin_df[clin_df['barcode'].notna() & clin_df['histological_type'].notna()]

# Exclude histological types enclosed in square brackets (any '[' or ']')
clin_df = clin_df[~clin_df['histological_type'].str.contains(r"\[|\]", regex=True)]

# Create mapping barcode -> histological_type
barcode_to_hist = clin_df.set_index('barcode')['histological_type'].to_dict()

# Clean igf2 df and convert normalized_count to float
igf2_df = igf2_df.rename(columns={"ParticipantBarcode": "barcode"})
igf2_df['normalized_count'] = pd.to_numeric(igf2_df['normalized_count'], errors='coerce')
igf2_df = igf2_df[igf2_df['normalized_count'].notna()]

# Filter IGF2 records to those present in LGG clinical barcodes
igf2_df = igf2_df[igf2_df['barcode'].isin(barcode_to_hist.keys())]

# If none, result is empty
if igf2_df.empty:
    result = {}
else:
    # Map histological type
    igf2_df['histology'] = igf2_df['barcode'].map(barcode_to_hist)
    # Compute log10(normalized_count + 1)
    igf2_df['log10_expr'] = igf2_df['normalized_count'].apply(lambda x: math.log10(x + 1))
    # Group by histology and compute mean
    grouped = igf2_df.groupby('histology')['log10_expr'].mean()
    # Format with at least four decimal places
    result = {hist: f"{val:.4f}" for hist, val in grouped.items()}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_keBRp7g861uAlG0jjX3ZRhZA': ['clinical_info'], 'var_call_AixUpJi16HglJPteEVLtrn7Q': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_sSmTlo9DYq5wQlAQaJ9keEEI': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_hllnPay0oAiICqic78iKG5Jz': 'file_storage/call_hllnPay0oAiICqic78iKG5Jz.json', 'var_call_UVUPK7amQst51vXaWgWbiQel': 'file_storage/call_UVUPK7amQst51vXaWgWbiQel.json'}

exec(code, env_args)
