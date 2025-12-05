code = """import json, pandas as pd

# Load full mutation data for CDH1
with open(var_call_5hJmgqSQhcwc3oLIurlIiZS4, 'r') as f:
    cdh1_mut = json.load(f)

# Load full BRCA clinical data
with open(var_call_A1xhZFollDNCeHNZYIFUsVb9, 'r') as f:
    brca_clin = json.load(f)

muts = pd.DataFrame(cdh1_mut)
clin = pd.DataFrame(brca_clin)

# Extract patient ID from Patient_description (e.g., 'patient TCGA-PE-A5DD (' -> TCGA-PE-A5DD)
clin['ParticipantBarcode'] = clin['Patient_description'].str.extract(r'patient (TCGA-[A-Z0-9\-]+)')

# Keep only alive patients (vital status in description contains 'Alive.')
clin_alive = clin[clin['Patient_description'].str.contains('vital status: Alive.', na=False)].copy()

# Determine which alive BRCA patients have CDH1 mutation
alive_ids = clin_alive['ParticipantBarcode'].dropna().unique()
mut_ids = muts['ParticipantBarcode'].dropna().unique()

clin_alive['CDH1_mutated'] = clin_alive['ParticipantBarcode'].isin(mut_ids)

# For each histological_type, compute percentage of patients with CDH1 mutation among alive patients
summary = (clin_alive.groupby('histological_type')['CDH1_mutated']
           .agg(['mean','count'])
           .rename(columns={'mean':'mutation_fraction','count':'alive_patients'})
           .reset_index())

# Filter to histological types with a reasonable number of alive patients (e.g., >=5) to avoid tiny groups
summary = summary[summary['alive_patients'] >= 5]

# Get top 3 histological types by mutation_fraction
top3 = summary.sort_values('mutation_fraction', ascending=False).head(3)

result = top3.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_5hJmgqSQhcwc3oLIurlIiZS4': 'file_storage/call_5hJmgqSQhcwc3oLIurlIiZS4.json', 'var_call_SXq4le3fbyEIX9SZE6wePC1w': ['clinical_info'], 'var_call_4tzc0gO4amGpsHNZpF46f0bj': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_A1xhZFollDNCeHNZYIFUsVb9': 'file_storage/call_A1xhZFollDNCeHNZYIFUsVb9.json'}

exec(code, env_args)
