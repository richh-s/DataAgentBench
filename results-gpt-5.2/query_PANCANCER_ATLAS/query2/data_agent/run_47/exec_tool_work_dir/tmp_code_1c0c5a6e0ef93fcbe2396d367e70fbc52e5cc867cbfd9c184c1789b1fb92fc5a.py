code = """import json, re, pandas as pd

# Load clinical breast records
path = var_call_FAJ9v9P35W29MmVBasTugfEd
with open(path, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)

# Extract ParticipantBarcode (TCGA-XX-YYYY) and vital status from Patient_description
pat_re = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(pat_re, expand=False)
clin_df['vital'] = clin_df['Patient_description'].str.extract(r'vital status\s*[:=]\s*(Alive|Dead)', expand=False)

# Keep alive only and valid barcode
alive = clin_df[(clin_df['vital'] == 'Alive') & (clin_df['ParticipantBarcode'].notna())].copy()

# Load CDH1 mutated participant list (deduplicate)
mut_path = var_call_p1QgTfsbKmPttoDs5rkiJCr7
with open(mut_path, 'r') as f:
    muts = json.load(f)
mut_df = pd.DataFrame(muts).drop_duplicates()
mut_set = set(mut_df['ParticipantBarcode'].dropna().unique().tolist())

alive['cdh1_mut'] = alive['ParticipantBarcode'].isin(mut_set)

# Compute per histological type: n_alive, n_mut, percent
agg = alive.groupby('histological_type', dropna=False).agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_cdh1_mut=('cdh1_mut','sum')
).reset_index()
agg['pct_cdh1_mut'] = (agg['n_cdh1_mut'] / agg['n_alive'] * 100).round(2)

# Only histological types with at least 1 alive patient
agg = agg[agg['n_alive'] > 0]

# Top 3 by percentage, tie-breaker by n_alive desc then n_mut desc
agg_sorted = agg.sort_values(['pct_cdh1_mut','n_alive','n_cdh1_mut','histological_type'], ascending=[False, False, False, True]).head(3)

result = agg_sorted.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_p1QgTfsbKmPttoDs5rkiJCr7': 'file_storage/call_p1QgTfsbKmPttoDs5rkiJCr7.json', 'var_call_E5tVAX0t2N6iNnpUByRXH4pH': ['clinical_info'], 'var_call_BeMYSXPwY4MrhcLsnm5iuyUk': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_rA6HprUvtAgFRsvZHi1aVRob': [], 'var_call_XB7lreEr7YiSLpqozoFjwU0m': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_FAJ9v9P35W29MmVBasTugfEd': 'file_storage/call_FAJ9v9P35W29MmVBasTugfEd.json'}

exec(code, env_args)
