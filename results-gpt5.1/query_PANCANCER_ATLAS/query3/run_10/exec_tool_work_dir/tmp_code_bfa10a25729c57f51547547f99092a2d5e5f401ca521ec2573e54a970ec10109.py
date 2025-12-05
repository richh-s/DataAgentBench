code = """import json, pandas as pd
from collections import defaultdict

# Load full clinical data
with open(var_call_qNAdTAZMsgqBR875BsA0N2Ti, 'r') as f:
    clinical = json.load(f)
clin_df = pd.DataFrame(clinical)

# Keep only BRCA patients and extract gender and barcode from Patient_description string
# BRCA = Breast invasive carcinoma according to hint typo, but we must parse acronyms from text.

def parse_acronym(desc: str):
    # look for pattern 'study of <Cancer>.' or 'diagnosed with <Cancer>.' and map BRCA keyword
    # but simpler: look for 'breast' (case-insensitive) to identify BRCA
    d = desc.lower()
    if 'breast' in d:
        return 'BRCA'
    return None

def parse_gender(desc: str):
    d = desc.upper()
    if ' MALE ' in d or d.startswith('MALE') or ' MALE,' in d:
        return 'MALE'
    if ' FEMALE ' in d or d.startswith('FEMALE') or ' FEMALE,' in d:
        return 'FEMALE'
    # also patterns 'is a FEMALE' etc already present
    if 'FEMALE' in d:
        return 'FEMALE'
    if 'MALE' in d:
        return 'MALE'
    return None

clin_df['cancer_type_acronym'] = clin_df['Patient_description'].apply(parse_acronym)
clin_df['gender'] = clin_df['Patient_description'].apply(parse_gender)

brca_female = clin_df[(clin_df['cancer_type_acronym']=='BRCA') & (clin_df['gender']=='FEMALE')].copy()

# Load CDH1 mutation data and keep reliable (FILTER == 'PASS')
with open(var_call_oimBkkVzkCDNRa1Wt3aDmkYd, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)
mut_pass = mut_df[mut_df['FILTER']=='PASS'].copy()

# CDH1 mutated patients set
mut_patients = set(mut_pass['ParticipantBarcode'].unique())

# Derive patient barcode from clinical Patient_description: pattern 'patient TCGA-..' or 'barcode TCGA-..'
import re

def extract_barcode(desc: str):
    m = re.search(r'TCGA-[A-Z0-9-]+', desc)
    return m.group(0) if m else None

brca_female['ParticipantBarcode'] = brca_female['Patient_description'].apply(extract_barcode)

# Drop rows without barcode
brca_female = brca_female[brca_female['ParticipantBarcode'].notna()].copy()

# Flag mutation presence
brca_female['CDH1_mut'] = brca_female['ParticipantBarcode'].isin(mut_patients)

# Build contingency table histological_type x CDH1_mut
cont = brca_female.groupby(['histological_type','CDH1_mut']).size().unstack(fill_value=0)

# Exclude categories (rows or cols) with marginal totals <=10
row_totals = cont.sum(axis=1)
col_totals = cont.sum(axis=0)
cont_filt = cont[(row_totals>10)]
cont_filt = cont_filt.loc[:, col_totals>10]

# If after filtering table is invalid (e.g., empty or one column/row), handle
if cont_filt.shape[0] == 0 or cont_filt.shape[1] != 2:
    result = {"error": "Insufficient data after filtering to compute chi-square with 2 mutation-status columns.",
              "table": cont.to_dict()}
else:
    # Compute chi-square statistic
    import numpy as np
    obs = cont_filt.values.astype(float)
    grand_total = obs.sum()
    row_tot = obs.sum(axis=1, keepdims=True)
    col_tot = obs.sum(axis=0, keepdims=True)
    expected = row_tot @ col_tot / grand_total
    chi2 = ((obs-expected)**2/expected).sum()
    result = {
        "chi_square_statistic": float(chi2),
        "contingency_table": cont_filt.to_dict(),
        "grand_total": float(grand_total)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oimBkkVzkCDNRa1Wt3aDmkYd': 'file_storage/call_oimBkkVzkCDNRa1Wt3aDmkYd.json', 'var_call_Gniwov4Mw6ElkxuSLBws4SLb': ['clinical_info'], 'var_call_BTJstQpOTBJUxk68BRN7VsrO': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_qNAdTAZMsgqBR875BsA0N2Ti': 'file_storage/call_qNAdTAZMsgqBR875BsA0N2Ti.json'}

exec(code, env_args)
