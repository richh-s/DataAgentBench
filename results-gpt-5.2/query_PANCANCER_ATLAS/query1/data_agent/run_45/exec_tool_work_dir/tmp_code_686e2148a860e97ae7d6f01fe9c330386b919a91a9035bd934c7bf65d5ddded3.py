code = """import json, re, math, pandas as pd

# Load clinical LGG histology list
p_clin = var_call_J4JXtvoVNH11wdp3siOMSWe8
if isinstance(p_clin, str):
    with open(p_clin, 'r') as f:
        clin = json.load(f)
else:
    clin = p_clin

df_clin = pd.DataFrame(clin)
# column names lowercased by postgres driver
barcode_col = [c for c in df_clin.columns if c.lower() in ('participantbarcode','participant_barcode','patient_description')][0]

# Extract TCGA barcode from description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['ParticipantBarcode'] = df_clin[barcode_col].astype(str).str.extract(pat, expand=False)
df_clin = df_clin.dropna(subset=['ParticipantBarcode','histological_type'])
# Exclude bracketed histology
mask_bracket = df_clin['histological_type'].astype(str).str.match(r'^\[.*\]$')
df_clin = df_clin[~mask_bracket]

# Load IGF2 expression
p_expr = var_call_Zo1Jy8OsnxS5VESqioTN1umC
if isinstance(p_expr, str):
    with open(p_expr, 'r') as f:
        expr = json.load(f)
else:
    expr = p_expr

df_expr = pd.DataFrame(expr)
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
df_expr = df_expr.dropna(subset=['ParticipantBarcode','normalized_count'])

# Merge; if multiple expression rows per participant, treat each sample independently (mean across samples)
df = df_expr.merge(df_clin[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

df['log10_expr'] = (df['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x>0 else float('nan'))
df = df.dropna(subset=['log10_expr'])

res = (df.groupby('histological_type', as_index=False)
         .agg(n_samples=('log10_expr','size'), avg_log10_igf2=('log10_expr','mean'))
      )
res['avg_log10_igf2'] = res['avg_log10_igf2'].map(lambda x: float(f"{x:.4f}"))
res = res.sort_values('histological_type')

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Zo1Jy8OsnxS5VESqioTN1umC': 'file_storage/call_Zo1Jy8OsnxS5VESqioTN1umC.json', 'var_call_Y2P3RYtUcxhfBnD7tidJTGpw': ['clinical_info'], 'var_call_X9RpfMsAdL9nPKNvokUSmAHn': [{'column_name': 'Patient_description'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'city_of_procurement'}, {'column_name': 'clinical_M'}, {'column_name': 'clinical_N'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_stage'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'diagnosis'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'ethnicity'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'form_completion_date'}, {'column_name': 'height'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_10'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'laterality'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'pathologic_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_stage'}, {'column_name': 'patient_death_reason'}, {'column_name': 'patient_id'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'prior_dx'}, {'column_name': 'prior_glioma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'race'}, {'column_name': 'radiation_therapy'}, {'column_name': 'residual_tumor'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'surgical_approach'}, {'column_name': 'system_version'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'tissue_source_site'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'venous_invasion'}, {'column_name': 'weight'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}], 'var_call_pj01rdZsnyDzVieQBlV76kxP': [], 'var_call_htZxlC8Buv1fOh1ytCIbB8Zm': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_nobul1GEXh1eqIxw7y6Y9MQB': [{'n_lgg': '0'}], 'var_call_0iK0OCp7oefrahoWbF063AYJ': [{'patient_id': '1953', 'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'patient_id': '1576', 'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'patient_id': '2408', 'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'patient_id': '2427', 'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'patient_id': '0933', 'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}], 'var_call_J4JXtvoVNH11wdp3siOMSWe8': 'file_storage/call_J4JXtvoVNH11wdp3siOMSWe8.json'}

exec(code, env_args)
