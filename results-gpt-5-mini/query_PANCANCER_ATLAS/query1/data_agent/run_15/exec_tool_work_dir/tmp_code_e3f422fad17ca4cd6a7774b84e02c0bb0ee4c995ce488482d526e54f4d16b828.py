code = """import json
import pandas as pd
import re
import math

# Load clinical LGG data
clinical_path = var_call_Bb2Z7N52XfaViK7kQenx7McZ
with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

# Load IGF2 RNASeq data
rna_path = var_call_HgPauQtpwHVCk5mPbMfHer6p
with open(rna_path, 'r') as f:
    rna_data = json.load(f)

clin_df = pd.DataFrame(clinical_data)
rna_df = pd.DataFrame(rna_data)

# Extract TCGA barcode from Patient_description using regex
pattern = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{1,4})')

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if not m:
        return None
    bc = m.group(1)
    # strip trailing punctuation
    bc = bc.strip('.,;()')
    return bc.upper()

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter clinical rows: have barcode and histological_type not null and not enclosed in square brackets
def valid_hist(h):
    if pd.isna(h):
        return False
    hstr = str(h).strip()
    # Exclude if contains [ or ] anywhere
    if '[' in hstr or ']' in hstr:
        return False
    # Exclude empty
    if hstr == '':
        return False
    return True

clin_df = clin_df[clin_df['ParticipantBarcode'].notna() & clin_df['histological_type'].apply(valid_hist)].copy()

# Normalize histological_type
clin_df['histological_type'] = clin_df['histological_type'].astype(str).str.strip()

# Prepare RNA data: ensure numeric normalized_count
rna_df = rna_df[rna_df['ParticipantBarcode'].notna()].copy()
# Convert normalized_count to float, coerce errors
rna_df['normalized_count'] = pd.to_numeric(rna_df['normalized_count'], errors='coerce')
rna_df = rna_df[rna_df['normalized_count'].notna()].copy()

# Keep only RNA rows for IGF2 (they should already be IGF2) and matching clinical barcodes
clin_barcodes = set(clin_df['ParticipantBarcode'].unique())
# Uppercase RNA barcodes
rna_df['ParticipantBarcode'] = rna_df['ParticipantBarcode'].astype(str).str.upper()

rna_df = rna_df[rna_df['ParticipantBarcode'].isin(clin_barcodes)].copy()

# Merge to attach histology
merged = pd.merge(rna_df, clin_df[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# If no merged rows, return empty
if merged.empty:
    result = {}
else:
    # Compute log10(normalized_count + 1)
    merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x+1) if x >= 0 else float('nan'))
    merged = merged[merged['log10_expr'].notna()]
    # Group by histological_type and compute mean
    grouped = merged.groupby('histological_type')['log10_expr'].mean().reset_index()
    # Format with at least four decimal places
    out = {}
    for _, row in grouped.sort_values('histological_type').iterrows():
        hist = row['histological_type']
        val = row['log10_expr']
        out[hist] = float(f"{val:.4f}")
    result = out

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7LCaJ6ebJsJ53ERNPmPBUWrH': ['clinical_info'], 'var_call_KIVsPktxrF3RxUpvgNmu3v5h': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_BMUWzQZCMqCyzK7sOzoXxRC7': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_AeJ3KTpBsNdafzogydOXwSmi': 'file_storage/call_AeJ3KTpBsNdafzogydOXwSmi.json', 'var_call_uVNOZBG35TygMrNheWvniIVU': 'file_storage/call_uVNOZBG35TygMrNheWvniIVU.json', 'var_call_Bb2Z7N52XfaViK7kQenx7McZ': 'file_storage/call_Bb2Z7N52XfaViK7kQenx7McZ.json', 'var_call_Ob5OGuPTweP0dkHvRZbpY4vd': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'SampleType', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Entrez', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'normalized_count', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_HgPauQtpwHVCk5mPbMfHer6p': 'file_storage/call_HgPauQtpwHVCk5mPbMfHer6p.json'}

exec(code, env_args)
