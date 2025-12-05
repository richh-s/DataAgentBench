code = """import json, pandas as pd
from pathlib import Path

# Load full mutation data
mut_path = var_call_S2NAmQXUlCLDTU0CoQjjtahJ
with open(mut_path, 'r') as f:
    mut_data = json.load(f)
mut_df = pd.DataFrame(mut_data)

# Keep only reliable mutation entries (FILTER == 'PASS') and unique patients
mut_df = mut_df[mut_df['FILTER'] == 'PASS'][['ParticipantBarcode']].drop_duplicates()
mut_df['CDH1_mut'] = 1

# Load clinical data
clin_path = var_call_uH44SyxUx80oh0LDuHYa8uQb
with open(clin_path, 'r') as f:
    clin_data = json.load(f)
clin_df = pd.DataFrame(clin_data)

# Extract patient barcode and gender from Patient_description via simple parsing
# Assume format contains 'patient TCGA-..-..' and 'FEMALE'/'MALE'
import re

def extract_barcode(desc):
    m = re.search(r'patient (TCGA-\S+)', desc)
    return m.group(1) if m else None

def extract_gender(desc):
    if ' FEMALE ' in desc or desc.strip().startswith('Patient') and ' FEMALE' in desc:
        return 'FEMALE'
    if ' MALE ' in desc or desc.strip().startswith('Patient') and ' MALE' in desc:
        return 'MALE'
    # fallback using ' a FEMALE' or ' a MALE'
    if ' a FEMALE' in desc:
        return 'FEMALE'
    if ' a MALE' in desc:
        return 'MALE'
    return None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)
clin_df['gender'] = clin_df['Patient_description'].apply(extract_gender)

# Filter to BRCA using hint: BRCA means Bladder urothelial carcinoma, but we don't have acronym column.
# Use icd_o_3_site patterns for breast (C50.x) to approximate BRCA and restrict to FEMALE.
clin_df_brca = clin_df[clin_df['icd_o_3_site'].str.startswith('C50', na=False)]
clin_df_brca_female = clin_df_brca[clin_df_brca['gender'] == 'FEMALE']

# Merge with mutation calls to get mutation presence (1) vs absence (0)
merged = clin_df_brca_female.merge(mut_df, left_on='barcode', right_on='ParticipantBarcode', how='left')
merged['CDH1_mut'] = merged['CDH1_mut'].fillna(0).astype(int)

# Build contingency table: histological_type x mutation (0/1)
ct = pd.crosstab(merged['histological_type'], merged['CDH1_mut'])

# Add marginal totals
row_totals = ct.sum(axis=1)
col_totals = ct.sum(axis=0)

# Exclude histological types with marginal totals <= 10
ct_filtered = ct[row_totals > 10]

# Recompute totals
row_totals = ct_filtered.sum(axis=1)
col_totals = ct_filtered.sum(axis=0)
N = ct_filtered.values.sum()

# Compute expected counts and chi-square statistic
import numpy as np
E = np.outer(row_totals.values, col_totals.values) / N
O = ct_filtered.values
chi2 = ((O - E)**2 / E).sum()

result = {
  'chi_square_statistic': float(chi2),
  'degrees_of_freedom': int((ct_filtered.shape[0]-1)*(ct_filtered.shape[1]-1)),
  'num_histological_types_used': int(ct_filtered.shape[0]),
  'total_patients_in_analysis': int(N)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S2NAmQXUlCLDTU0CoQjjtahJ': 'file_storage/call_S2NAmQXUlCLDTU0CoQjjtahJ.json', 'var_call_UUNssn6JobEJSGhVRTovpfHO': ['clinical_info'], 'var_call_bqBu5q0IS5KLobf09VCHcaAI': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_uH44SyxUx80oh0LDuHYa8uQb': 'file_storage/call_uH44SyxUx80oh0LDuHYa8uQb.json'}

exec(code, env_args)
