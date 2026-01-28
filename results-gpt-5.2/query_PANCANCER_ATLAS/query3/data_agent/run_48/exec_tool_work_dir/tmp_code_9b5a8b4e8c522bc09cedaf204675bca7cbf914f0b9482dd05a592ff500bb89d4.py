code = """import json, re, pandas as pd

# Load clinical records
path_clin = var_call_pgYOp35XvaJAda7iyhILwV64
with open(path_clin, 'r') as f:
    clin = json.load(f)

df_clin = pd.DataFrame(clin)
# extract TCGA barcode from text
pat = re.compile(r"(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})")
df_clin['participant_barcode'] = df_clin['participant_barcode'].apply(lambda s: pat.search(s).group(1) if isinstance(s,str) and pat.search(s) else None)
df_clin = df_clin.dropna(subset=['participant_barcode','histological_type']).drop_duplicates(subset=['participant_barcode'])

# Load mutation PASS CDH1
path_mut = var_call_2xigF5CsjX6b1V3cUbkLaEwg
with open(path_mut, 'r') as f:
    mut = json.load(f)
df_mut = pd.DataFrame(mut)
df_mut = df_mut.dropna(subset=['participant_barcode'])
# presence per patient
mut_pat = df_mut.groupby('participant_barcode').size().rename('n_mut').reset_index()
mut_pat['CDH1_mut'] = 1
mut_pat = mut_pat[['participant_barcode','CDH1_mut']]

# Merge and define mutation status
merged = df_clin.merge(mut_pat, on='participant_barcode', how='left')
merged['CDH1_mut'] = merged['CDH1_mut'].fillna(0).astype(int)

# contingency table
ct = pd.crosstab(merged['histological_type'], merged['CDH1_mut'])
ct.columns = ['no_mut','mut']

# Exclude categories with marginal totals <=10
ct['row_total'] = ct.sum(axis=1)
ct_f = ct[ct['row_total']>10].drop(columns=['row_total'])

# also exclude columns if marginal totals <=10
col_totals = ct_f.sum(axis=0)
keep_cols = [c for c in ct_f.columns if col_totals[c]>10]
ct_f = ct_f[keep_cols]

# compute chi-square
O = ct_f.values.astype(float)
row_tot = O.sum(axis=1, keepdims=True)
col_tot = O.sum(axis=0, keepdims=True)
grand = O.sum()
E = row_tot.dot(col_tot)/grand
chi2 = float(((O-E)**2/E).sum())
dof = int((O.shape[0]-1)*(O.shape[1]-1))

result = {
    'chi_square': chi2,
    'degrees_of_freedom': dof,
    'grand_total': int(grand),
    'categories_used': int(O.shape[0]),
    'contingency_table': ct_f.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2xigF5CsjX6b1V3cUbkLaEwg': 'file_storage/call_2xigF5CsjX6b1V3cUbkLaEwg.json', 'var_call_nJMheo342ZX9xQt66KCmp3GO': ['clinical_info'], 'var_call_IQXlPsq1NrK0mOefbqp5d3c9': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_u89c3jS4gUatrJzoQqfcdLSn': [{'n': '1087', 'example': 'Case 00807dae-9f4a-4fd1-aac2-82eb11bf2afb, linked to barcode TCGA-A2-A04W, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.'}], 'var_call_pgYOp35XvaJAda7iyhILwV64': 'file_storage/call_pgYOp35XvaJAda7iyhILwV64.json'}

exec(code, env_args)
