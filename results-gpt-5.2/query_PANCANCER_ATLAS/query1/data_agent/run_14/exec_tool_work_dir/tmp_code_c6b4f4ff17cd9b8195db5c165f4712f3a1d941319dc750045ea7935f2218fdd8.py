code = """import json, re, math
import pandas as pd

# Load IGF2 expression (may be large)
expr_src = var_call_VTD9o1qxchk6OAwlTLsFdooS
if isinstance(expr_src, str) and expr_src.endswith('.json'):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src

clin_src = var_call_HRpyBvbZAZVNHlENhC4o1WT7
if isinstance(clin_src, str) and clin_src.endswith('.json'):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

expr_df = pd.DataFrame(expr)
# coerce to float
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count','ParticipantBarcode'])

# compute log10(normalized_count+1)
expr_df['log10_igf2'] = (expr_df['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x>0 else float('nan'))
expr_df = expr_df.dropna(subset=['log10_igf2'])

clin_df = pd.DataFrame(clin)
# parse barcode from Patient_description
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(lambda s: (pat.search(s).group(1) if isinstance(s,str) and pat.search(s) else None))
clin_df = clin_df.dropna(subset=['ParticipantBarcode','histological_type'])

# filter histology not enclosed in square brackets (entire string)
clin_df = clin_df[~clin_df['histological_type'].astype(str).str.match(r'^\s*\[.*\]\s*$')]

# join
merged = expr_df.merge(clin_df[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# average per histology
res = merged.groupby('histological_type', as_index=False).agg(
    n=('log10_igf2','size'),
    avg_log10_igf2=('log10_igf2','mean')
)
res['avg_log10_igf2'] = res['avg_log10_igf2'].round(6)
res = res.sort_values('histological_type')

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VTD9o1qxchk6OAwlTLsFdooS': 'file_storage/call_VTD9o1qxchk6OAwlTLsFdooS.json', 'var_call_qTVLrE13kefDofXHX2mqa2kP': [{'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}], 'var_call_PqRg15HohQaEPkZmarv33rnR': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}], 'var_call_K3oyZV6Rcl9iszAZztUzjbGZ': [], 'var_call_10EUlx5HPTFarPjNZb9jNxcc': [], 'var_call_agXuztMmAjXqJpzvT1DFJX02': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_d0A2SBSsms0KfCYhV5acAu0x': [{'dataset_part': "Patient TCGA-EA-A3Y4, registered under UUID 3AC62513-B5F4-4063-AABD-DAD08A1F56FB, belongs to the Cervical squamous cell carcinoma and endocervical adenocarcinoma cohort. This FEMALE patient's vital status is Alive."}, {'dataset_part': 'Patient TCGA-B6-A0IJ (FEMALE, UUID 2c86c3ea-d926-4d39-a5ae-39ece4774287) is enrolled in the study of Breast invasive carcinoma. Vital status: Alive.'}, {'dataset_part': 'Patient TCGA-BJ-A3PT (FEMALE, UUID 29C4319C-3EAD-42B1-810D-418DA8D515C4) is enrolled in the study of Thyroid carcinoma. Vital status: Alive.'}, {'dataset_part': 'Patient TCGA-AG-A015 (FEMALE, UUID 09daff79-6493-45c1-8cba-9381259e2bea) is enrolled in the study of Rectum adenocarcinoma. Vital status: Alive.'}, {'dataset_part': 'Case 1D75E89D-4B01-443C-BE54-749C7A667BF4, linked to barcode TCGA-LL-A5YL, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.'}, {'dataset_part': 'The individual with barcode TCGA-DS-A1O9 and UUID b8eae533-2ad6-4dcf-98af-0fe7ff23a879 is a FEMALE case of Cervical squamous cell carcinoma and endocervical adenocarcinoma, documented with vital status = Dead.'}, {'dataset_part': 'Case E3905D75-9D0A-4981-AB42-83CE2C20C4EA, linked to barcode TCGA-FR-A7UA, corresponds to a FEMALE patient diagnosed with Skin Cutaneous Melanoma, with vital status Alive.'}, {'dataset_part': 'Clinical entry ac67d0df-7dc0-4a1a-8b47-beec9b94de86 identifies patient TCGA-CH-5745, a MALE subject with Prostate adenocarcinoma. Their current vital status is Alive.'}, {'dataset_part': "Patient TCGA-CV-7097, registered under UUID 9d0f5938-6a01-4c06-8536-dff834f7f2f9, belongs to the Head and Neck squamous cell carcinoma cohort. This MALE patient's vital status is Dead."}, {'dataset_part': "Patient TCGA-BH-A1EW, registered under UUID 9d166970-07c8-4ca3-9cfa-ed0049df9ecc, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Dead."}, {'dataset_part': "Patient TCGA-QR-A6H4, registered under UUID 38D7C7A6-C907-4F9B-AD34-47776E5BABDD, belongs to the Pheochromocytoma and Paraganglioma cohort. This FEMALE patient's vital status is Alive."}, {'dataset_part': 'Record E0DFC37A-4A2E-4353-9673-241B100B3467 refers to patient TCGA-V1-A9O5, a MALE diagnosed with Prostate adenocarcinoma. Vital status recorded as Alive.'}, {'dataset_part': 'Patient TCGA-ET-A2N5 (FEMALE, UUID 7D818F01-49A6-4BA8-9F1C-C77398ADBDD0) is enrolled in the study of Thyroid carcinoma. Vital status: Alive.'}, {'dataset_part': 'Patient TCGA-AO-A126 (FEMALE, UUID cc0902fd-a2fc-4327-929e-d4219e32e1d7) is enrolled in the study of Breast invasive carcinoma. Vital status: Alive.'}, {'dataset_part': 'The individual with barcode TCGA-CJ-4893 and UUID d65f7f50-2cb0-45e7-866a-ba5c498aef52 is a FEMALE case of Kidney renal clear cell carcinoma, documented with vital status = Alive.'}, {'dataset_part': "Patient TCGA-DT-5265, registered under UUID 3f10de1e-c8ce-415e-b4e1-e50901686a2f, belongs to the Rectum adenocarcinoma cohort. This MALE patient's vital status is Alive."}, {'dataset_part': 'Patient TCGA-50-5931 (UUID 12ccd581-a921-41bc-bcee-4e9be54532cc) is a FEMALE diagnosed with Lung adenocarcinoma. Current vital status: Dead.'}, {'dataset_part': 'Patient TCGA-BA-5557 (FEMALE, UUID 7e0575ce-670b-4035-8a90-4d35279707b2) is enrolled in the study of Head and Neck squamous cell carcinoma. Vital status: Alive.'}, {'dataset_part': 'Patient TCGA-Q9-A6FW (UUID C89F6EA5-786D-4D3C-AA93-681664A908F9) is a MALE diagnosed with Esophageal carcinoma. Current vital status: Alive.'}, {'dataset_part': 'Patient TCGA-VS-A94X (FEMALE, UUID 240EF385-DECC-48F7-A798-A81B4AB0410E) is enrolled in the study of Cervical squamous cell carcinoma and endocervical adenocarcinoma. Vital status: Dead.'}], 'var_call_HRpyBvbZAZVNHlENhC4o1WT7': 'file_storage/call_HRpyBvbZAZVNHlENhC4o1WT7.json'}

exec(code, env_args)
