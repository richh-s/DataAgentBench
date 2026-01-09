code = """import json, re, pandas as pd, numpy as np

# Load clinical brain patients (includes LGG+GBM etc). We'll filter to LGG by excluding GBM terms.
path_clin = var_call_EkLf6cKiEFGctgrYWny3pJkP
with open(path_clin, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)

# Extract TCGA barcode from Patient_description text
clin_df['participant_barcode'] = clin_df['participant'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)

# Filter out missing barcode
clin_df = clin_df[clin_df['participant_barcode'].notna()].copy()

# Keep histology not enclosed in square brackets (exactly like [Not Applicable] etc)
clin_df['histology'] = clin_df['histology'].astype(str)
clin_df = clin_df[~clin_df['histology'].str.match(r'^\s*\[.*\]\s*$', na=False)].copy()

# Approximate LGG cohort: exclude Glioblastoma / GBM mentions in patient description OR histology
is_gbm = clin_df['participant'].str.contains('Glioblastoma', case=False, na=False) | clin_df['histology'].str.contains('GBM|Glioblastoma', case=False, na=False)
clin_df = clin_df[~is_gbm].copy()

# Load IGF2 expression
path_expr = var_call_uYbluSf1r4BnWcjkwonxmY4j
with open(path_expr, 'r') as f:
    expr = json.load(f)
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df[expr_df['normalized_count'].notna()].copy()
expr_df['participant'] = expr_df['participant'].astype(str)

# Join on barcode
merged = clin_df.merge(expr_df, left_on='participant_barcode', right_on='participant', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1.0)

# Average across samples per histology type (mean of all matched rows)
out = (merged.groupby('histology', as_index=False)
       .agg(avg_log10_igf2=('log10_expr','mean'), n=('log10_expr','size'))
       .sort_values('avg_log10_igf2', ascending=False))

# Format with at least 4 decimals
out['avg_log10_igf2'] = out['avg_log10_igf2'].map(lambda x: float(f"{x:.4f}"))

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iF5csqMHKohz083mWeSnqgxP': ['clinical_info'], 'var_call_r83JVnt62YbUnC5XUFN4nBnO': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_MMPK6xdjtS6fvuvDVVGnV8TP': [{'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'pathologic_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_stage'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}], 'var_call_uYbluSf1r4BnWcjkwonxmY4j': 'file_storage/call_uYbluSf1r4BnWcjkwonxmY4j.json', 'var_call_vp5eNFoG0V2eXT2KznDFD97M': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_wJ3HPghkW3GYrHllC4qtqrgm': [], 'var_call_zu6TV4tE8THbZx7Tlg6VfRow': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_RHzAtJOJzt5DlzzAmXAtI3nj': [], 'var_call_ucmwXbj0bl03gPIZyUeofiRf': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_3SvQGeGevAYnDpkAf3yrTUwD': [{'tissue_site': 'Breast', 'n': '1087'}, {'tissue_site': 'Lung', 'n': '1004'}, {'tissue_site': 'Kidney', 'n': '869'}, {'tissue_site': 'Brain', 'n': '590'}, {'tissue_site': 'Ovary', 'n': '579'}, {'tissue_site': 'Head and Neck', 'n': '560'}, {'tissue_site': 'Endometrial', 'n': '530'}, {'tissue_site': 'Central nervous system', 'n': '513'}, {'tissue_site': 'Thyroid', 'n': '503'}, {'tissue_site': 'Prostate', 'n': '495'}, {'tissue_site': 'Colon', 'n': '442'}, {'tissue_site': 'Stomach', 'n': '440'}, {'tissue_site': 'Bladder', 'n': '412'}, {'tissue_site': 'Liver', 'n': '374'}, {'tissue_site': 'Cervical', 'n': '306'}, {'tissue_site': 'Extremities', 'n': '193'}, {'tissue_site': 'Pancreas', 'n': '184'}, {'tissue_site': 'Esophagus', 'n': '183'}, {'tissue_site': 'Trunk', 'n': '169'}, {'tissue_site': 'Rectum', 'n': '156'}, {'tissue_site': 'Adrenal gland', 'n': '146'}, {'tissue_site': 'Testes', 'n': '133'}, {'tissue_site': 'None', 'n': '100'}, {'tissue_site': 'Thymus', 'n': '97'}, {'tissue_site': 'Adrenal', 'n': '91'}, {'tissue_site': 'Pleura', 'n': '87'}, {'tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tissue_site': 'Uterus', 'n': '57'}, {'tissue_site': 'Choroid', 'n': '56'}, {'tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}, {'tissue_site': 'Bile duct', 'n': '36'}, {'tissue_site': 'Extra-adrenal Site', 'n': '32'}, {'tissue_site': 'Anterior Mediastinum', 'n': '27'}, {'tissue_site': 'Gynecological - Uterus', 'n': '25'}, {'tissue_site': 'Choroid|Ciliary body', 'n': '22'}, {'tissue_site': 'Lower Extremity - Lower leg/calf', 'n': '17'}, {'tissue_site': 'Other  Specify', 'n': '14'}, {'tissue_site': 'Lower abdominal/Pelvic - Pelvic', 'n': '9'}, {'tissue_site': 'Upper Extremity - Shoulder/axilla', 'n': '7'}, {'tissue_site': 'Retroperitoneum/Upper abdominal - Kidney', 'n': '7'}, {'tissue_site': 'Chest - Chest wall', 'n': '7'}, {'tissue_site': 'Superficial Trunk - Back', 'n': '5'}, {'tissue_site': 'Upper Extremity - Upper arm/elbow', 'n': '5'}, {'tissue_site': '[Unknown]', 'n': '5'}, {'tissue_site': 'Lower Extremity - Foot/ankle', 'n': '4'}, {'tissue_site': 'Lower Extremity - Other (please specify', 'n': '4'}, {'tissue_site': 'Retroperitoneum/Upper abdominal - Colon', 'n': '4'}, {'tissue_site': 'Superficial Trunk - Buttock', 'n': '4'}, {'tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal', 'n': '3'}, {'tissue_site': 'Omentum', 'n': '3'}], 'var_call_EkLf6cKiEFGctgrYWny3pJkP': 'file_storage/call_EkLf6cKiEFGctgrYWny3pJkP.json'}

exec(code, env_args)
