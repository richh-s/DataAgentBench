code = """import json, math, pandas as pd

# Load clinical LGG histology records
clin_src = var_call_BCIRAcxnOIDHWUUt1LGwW8Jv
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# Load IGF2 expression records
expr_src = var_call_SWvfFU5keacC8wheFg58rEuq
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src

df_clin = pd.DataFrame(clin)
df_expr = pd.DataFrame(expr)

# Ensure numeric
for col in ['normalized_count']:
    if col in df_expr.columns:
        df_expr[col] = pd.to_numeric(df_expr[col], errors='coerce')

# Compute log10(normalized_count + 1)
df_expr = df_expr.dropna(subset=['participant_barcode','normalized_count'])
df_expr = df_expr[df_expr['normalized_count'] >= 0]
df_expr['log10_expr'] = (df_expr['normalized_count'] + 1.0).apply(lambda x: math.log10(x))

# If multiple samples per participant, average per participant first
per_pt = df_expr.groupby('participant_barcode', as_index=False)['log10_expr'].mean()

# Join to histology
merged = per_pt.merge(df_clin.dropna(subset=['participant_barcode','histology']), on='participant_barcode', how='inner')

# Group by histology and compute mean
res = merged.groupby('histology', as_index=False).agg(n_patients=('participant_barcode','nunique'), avg_log10_igf2=('log10_expr','mean'))
res = res.sort_values('histology')

# Format with >=4 decimal places
out_lines = []
for _, r in res.iterrows():
    out_lines.append(f"{r['histology']}: {r['avg_log10_igf2']:.4f} (n={int(r['n_patients'])})")
answer = "\n".join(out_lines)

print('__RESULT__:')
print(json.dumps({'answer': answer}))"""

env_args = {'var_call_SWvfFU5keacC8wheFg58rEuq': 'file_storage/call_SWvfFU5keacC8wheFg58rEuq.json', 'var_call_tbZUselfI7ruV7PEjlDVthaS': ['clinical_info'], 'var_call_ovRfGR0Y8sndB0AmOIc35Glw': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_kYUVcv9FJN5h9Z7hal6UoTeX': [], 'var_call_lq97EOH2d6fvhKSq1wTjKxoq': [{'participant_barcode': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histology': 'Oligodendroglioma'}, {'participant_barcode': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histology': 'Oligoastrocytoma'}, {'participant_barcode': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histology': 'Oligoastrocytoma'}, {'participant_barcode': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histology': 'Oligoastrocytoma'}, {'participant_barcode': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histology': 'Oligoastrocytoma'}], 'var_call_BCIRAcxnOIDHWUUt1LGwW8Jv': 'file_storage/call_BCIRAcxnOIDHWUUt1LGwW8Jv.json'}

exec(code, env_args)
