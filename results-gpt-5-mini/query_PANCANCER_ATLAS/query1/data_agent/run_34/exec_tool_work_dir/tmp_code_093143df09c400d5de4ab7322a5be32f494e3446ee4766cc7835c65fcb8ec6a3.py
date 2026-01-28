code = """import json
# var_call_SXRaVcwVFZGlKmeqNoVkA1yC already holds a dict result from previous execute_python printed output
# but storage variables are only set to tool outputs; we need to re-open the file containing the output
# The earlier execute_python prints are stored; however we can instead re-run the processing to produce the final print only

import pandas as pd
import re
import numpy as np

# Load clinical data
clin_var = var_call_2WLFTOAzW8128zWPmtrs0zT0
if isinstance(clin_var, str):
    with open(clin_var, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_var

# Load molecular data
mol_var = var_call_srFGL36CbBwqMzpw8oSLgMAe
if isinstance(mol_var, str):
    with open(mol_var, 'r') as f:
        mol = json.load(f)
else:
    mol = mol_var

clin_df = pd.DataFrame(clin)
mol_df = pd.DataFrame(mol)

pattern = re.compile(r"TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4}")

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(0) if m else None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter entries that are LGG via Patient_description containing 'Brain lower grade glioma'
clin_df = clin_df[clin_df['Patient_description'].str.contains('Brain lower grade glioma', na=False)]

# Filter histological_type not enclosed in square brackets
clin_df = clin_df[clin_df['histological_type'].apply(lambda h: isinstance(h, str) and not (h.strip().startswith('[') and h.strip().endswith(']')))]

# prepare molecular
mol_df['pb'] = mol_df['ParticipantBarcode'].astype(str).str.slice(0,12)
mol_df['normalized_count'] = pd.to_numeric(mol_df['normalized_count'], errors='coerce')
mol_df = mol_df[mol_df['normalized_count'].notna()]

clin_df['pb'] = clin_df['barcode'].str.slice(0,12)
merged = pd.merge(clin_df[['pb','histological_type']], mol_df[['pb','normalized_count']], on='pb', how='inner')
merged['log10_val'] = np.log10(merged['normalized_count'] + 1)

grouped = merged.groupby('histological_type')['log10_val'].mean().reset_index()
out = {row['histological_type']: float(f"{row['log10_val']:.6f}") for _, row in grouped.iterrows()}
out_sorted = {k: out[k] for k in sorted(out.keys())}

print("__RESULT__:")
print(json.dumps(out_sorted))"""

env_args = {'var_call_wIwc53NAaDinBHPx0hURH0ht': ['clinical_info'], 'var_call_G7ie5ATmvnugCrOc8KsHRXPg': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_wJZbMCMKO0tA5ed2QohBQ95u': 'file_storage/call_wJZbMCMKO0tA5ed2QohBQ95u.json', 'var_call_EBg0JlGC0WerpaFHO4XgZI5D': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_2WLFTOAzW8128zWPmtrs0zT0': 'file_storage/call_2WLFTOAzW8128zWPmtrs0zT0.json', 'var_call_srFGL36CbBwqMzpw8oSLgMAe': 'file_storage/call_srFGL36CbBwqMzpw8oSLgMAe.json', 'var_call_SXRaVcwVFZGlKmeqNoVkA1yC': {'Astrocytoma': 2.571298, 'Oligoastrocytoma': 2.713571, 'Oligodendroglioma': 2.682458, 'Paraganglioma; Extra-adrenal Pheochromocytoma': 5.557095, 'Pheochromocytoma': 5.011716}}

exec(code, env_args)
