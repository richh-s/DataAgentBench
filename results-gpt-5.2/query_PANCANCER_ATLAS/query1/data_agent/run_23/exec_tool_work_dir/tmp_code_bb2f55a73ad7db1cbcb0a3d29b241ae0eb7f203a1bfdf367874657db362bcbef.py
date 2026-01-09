code = """import json, re, math, pandas as pd

# Load clinical records
clin_src = var_call_zh8sZRtfUbNhSLiLjwVw7VDV
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# Extract TCGA barcode from Patient_description text
rows=[]
pat=re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
for r in clin:
    txt = r.get('participant_barcode')
    m = pat.search(txt or '')
    if not m:
        continue
    rows.append({'participant_barcode': m.group(1), 'histology': r.get('histology')})
clin_df=pd.DataFrame(rows).dropna()

# Load expression records
expr_src = var_call_Qu8jlYoy5Xcgq4Q0xtn1Yjcv
if isinstance(expr_src, str):
    with open(expr_src,'r') as f:
        expr=json.load(f)
else:
    expr=expr_src
expr_df=pd.DataFrame(expr)
expr_df['normalized_count']=pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df=expr_df.dropna(subset=['participant_barcode','normalized_count'])

# Merge and compute log10(x+1)
merged = clin_df.merge(expr_df, on='participant_barcode', how='inner')
merged = merged.dropna(subset=['histology','normalized_count'])
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x))

out = (merged.groupby('histology', as_index=False)
       .agg(avg_log10_igf2=('log10_expr','mean'), n=('log10_expr','size'))
       .sort_values('histology'))

out['avg_log10_igf2'] = out['avg_log10_igf2'].map(lambda v: float(f"{v:.4f}"))
result = out[['histology','avg_log10_igf2']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Qu8jlYoy5Xcgq4Q0xtn1Yjcv': 'file_storage/call_Qu8jlYoy5Xcgq4Q0xtn1Yjcv.json', 'var_call_JZXtKJqswU5D7XCft7J5rZ1g': ['clinical_info'], 'var_call_PaNJHU9QhOlJO1c5Ng9rQxxC': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_PI34u1PlwCQpKhLp7srjB08a': [], 'var_call_06TzOyPv3AwAmRSJWBFsLwb8': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_mCCiBkMlRIWJdzvz5wq6VCcA': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_u8ftLvPUYeXJgfkKlJsw3Sfb': [{'tumor_tissue_site': 'Brain', 'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'tumor_tissue_site': 'Brain', 'histological_type': 'Glioblastoma Multiforme (GBM)', 'n': '31'}, {'tumor_tissue_site': 'Brain', 'histological_type': 'Treated primary GBM', 'n': '20'}], 'var_call_jCJ1E3DwCOubtIIaKUu9Sf4s': [{'tumor_tissue_site': 'Brain', 'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'tumor_tissue_site': 'Brain', 'histological_type': 'Glioblastoma Multiforme (GBM)', 'n': '31'}, {'tumor_tissue_site': 'Brain', 'histological_type': 'Treated primary GBM', 'n': '20'}, {'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Astrocytoma', 'n': '194'}, {'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligodendroglioma', 'n': '189'}, {'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligoastrocytoma', 'n': '130'}], 'var_call_zh8sZRtfUbNhSLiLjwVw7VDV': 'file_storage/call_zh8sZRtfUbNhSLiLjwVw7VDV.json'}

exec(code, env_args)
