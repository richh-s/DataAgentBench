code = """import json
import pandas as pd
import re
with open(var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L, 'r') as f:
    clinical = json.load(f)
df = pd.DataFrame(clinical)

patterns = ['lower grade', 'LGG', 'lower-grade', 'lowergrade', 'lower', 'glioma', 'brain lower', 'Brain lower']
results = {}
for p in patterns:
    mask = df['Patient_description'].astype(str).str.contains(p, case=False, na=False)
    results[p] = int(mask.sum())

# Also show some sample Patient_description entries that contain 'Brain' and 'Glioma'
mask_brain = df['Patient_description'].astype(str).str.contains('brain', case=False, na=False)
sample_brain = df.loc[mask_brain, 'Patient_description'].astype(str).unique()[:20].tolist()
mask_glioma = df['Patient_description'].astype(str).str.contains('glioma', case=False, na=False)
sample_glioma = df.loc[mask_glioma, 'Patient_description'].astype(str).unique()[:20].tolist()

import json as _json
print('__RESULT__:')
print(_json.dumps({'pattern_counts': results, 'sample_brain': sample_brain, 'sample_glioma': sample_glioma}))"""

env_args = {'var_call_BnOs3qTuUKJVm1yYaAwIGg6B': ['clinical_info'], 'var_call_Xb1mga1kcDrxacJ3WHx7OOWy': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CQrglBnFJ3kAKzT9XuJNu14U': 'file_storage/call_CQrglBnFJ3kAKzT9XuJNu14U.json', 'var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L': 'file_storage/call_Tfg7buZ6AcKLZPqZ1Zjppr8L.json', 'var_call_SiJXcvDVIVobhLvoiappQcjN': {}, 'var_call_Bt8HpIg7jEjefycKMB6Sn15g': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'matched_samples': {'icd_o_3_site': ['C56.9', 'C71.9', 'C48.1', 'C48.2'], 'tumor_tissue_site': ['Ovary', 'Brain', 'Omentum', 'Peritoneum ovary'], 'new_tumor_event_after_initial_treatment': ['None', 'NO', 'YES', '[Unknown]'], 'person_neoplasm_cancer_status': ['WITH TUMOR', 'None', 'TUMOR FREE'], 'histological_type': ['Serous Cystadenocarcinoma', 'Treated primary GBM', 'Untreated primary (de novo) GBM'], 'tissue_source_site': ['31', '36', '25', '29', '10', '23', 'WR', '32', '57', '04'], 'eastern_cancer_oncology_group': ['1', '2', 'None', '0', '4'], 'residual_tumor': ['None', 'R1', 'R0'], 'histological_type_other': ['None'], 'tumor_tissue_site_other': ['None'], 'axillary_lymph_node_stage_method_type': ['None'], 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': ['None'], 'days_to_new_tumor_event_after_initial_treatment': ['None'], 'family_history_of_cancer': ['None']}}}

exec(code, env_args)
