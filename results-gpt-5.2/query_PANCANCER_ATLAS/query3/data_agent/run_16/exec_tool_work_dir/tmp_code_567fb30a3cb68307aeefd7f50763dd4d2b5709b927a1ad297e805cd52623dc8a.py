code = """import json, re, pandas as pd

# Load clinical records
path = var_call_FndWmFjxzprS7uH3zicCBwPC
with open(path, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)

# Extract TCGA barcode from participant_barcode string
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['tcga'] = clin_df['participant_barcode'].astype(str).str.extract(pat, expand=False)
clin_df = clin_df.dropna(subset=['tcga'])
clin_df['histological_type'] = clin_df['histological_type'].astype(str).str.strip()
clin_df = clin_df[clin_df['histological_type']!='']

# mutation participants list (CDH1 reliable)
mut_path = var_call_aR14ibDYkLuRLRcCezrUJJtA
with open(mut_path, 'r') as f:
    muts = json.load(f)
mut_set = set([r['participant_barcode'] for r in muts if r.get('participant_barcode')])

# Build contingency table: histological_type vs mutated (1/0)
clin_df['cdh1_mut'] = clin_df['tcga'].isin(mut_set).astype(int)

tab = pd.crosstab(clin_df['histological_type'], clin_df['cdh1_mut'])
# ensure both columns 0 and 1 exist
for c in [0,1]:
    if c not in tab.columns:
        tab[c]=0

tab = tab[[0,1]]

# Exclude categories with marginal totals <=10 (row totals)
row_totals = tab.sum(axis=1)
filtered = tab.loc[row_totals > 10].copy()

# Also ensure column totals >10? prompt says categories with marginal totals <=10; apply to both rows and columns
col_totals = filtered.sum(axis=0)
filtered = filtered.loc[:, col_totals > 10]

# Compute chi-square
O = filtered.to_numpy(dtype=float)
row_sum = O.sum(axis=1, keepdims=True)
col_sum = O.sum(axis=0, keepdims=True)
grand = O.sum()
E = row_sum @ col_sum / grand
chi2 = float(((O - E)**2 / E).sum())

out = {
    'chi_square': chi2,
    'grand_total': int(grand),
    'rows_included': int(filtered.shape[0]),
    'cols_included': [str(c) for c in filtered.columns.tolist()],
    'contingency_table': filtered.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aR14ibDYkLuRLRcCezrUJJtA': 'file_storage/call_aR14ibDYkLuRLRcCezrUJJtA.json', 'var_call_qlP6TdBlTiLkkIuYlg1rm3pH': [{'participant_barcode': 'TCGA-A8-A091', 'filter': 'wga'}, {'participant_barcode': 'TCGA-A8-A0A1', 'filter': 'wga'}, {'participant_barcode': 'TCGA-A8-A0A9', 'filter': 'wga'}, {'participant_barcode': 'TCGA-AA-3821', 'filter': 'wga'}, {'participant_barcode': 'TCGA-A2-A0YL', 'filter': 'PASS'}], 'var_call_U4IARSnPjYv65nk21VGMkrq3': [{'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'neoplasm_histologic_grade'}], 'var_call_njGBj8d82cwtW02085XBjvF6': [], 'var_call_6ImZu3WdwsJjuZrLszLNz8jB': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_3GCm4KDVgpdWuVjqsMf7lFc2': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_X4uPX8gWYX6LLEnGid9OtGJq': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_FndWmFjxzprS7uH3zicCBwPC': 'file_storage/call_FndWmFjxzprS7uH3zicCBwPC.json'}

exec(code, env_args)
