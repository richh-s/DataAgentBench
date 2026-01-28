code = """import json, re, pandas as pd

# Load clinical records
clin_src = var_call_P17U7fLhQQujtLUkI1qhzYN2
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# Load mutation carriers (CDH1, PASS)
mut_src = var_call_dGqGzP3NQBexBimZHNt0AeZD
if isinstance(mut_src, str):
    with open(mut_src, 'r') as f:
        muts = json.load(f)
else:
    muts = mut_src

mut_set = set(r['participant_barcode'] for r in muts if r.get('participant_barcode') is not None)

# Extract TCGA barcode from Patient_description text
pat_re = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
rows = []
for r in clin:
    desc = r.get('participant_barcode','')
    m = pat_re.search(desc or '')
    if not m:
        continue
    bc = m.group(1)
    hist = r.get('histological_type')
    if hist is None:
        continue
    hist = str(hist).strip()
    if hist == '' or hist.lower() in {'none','[not applicable]','not reported','nan'}:
        continue
    rows.append({'participant_barcode': bc, 'histological_type': hist, 'cdh1_mut': 1 if bc in mut_set else 0})

df = pd.DataFrame(rows).drop_duplicates(subset=['participant_barcode'])

# Build contingency table
ct = pd.crosstab(df['histological_type'], df['cdh1_mut'])
# Ensure both columns exist
for c in [0,1]:
    if c not in ct.columns:
        ct[c] = 0
ct = ct[[0,1]]

# Exclude histology categories with marginal totals <= 10
ct = ct.loc[ct.sum(axis=1) > 10]

# Also drop columns with totals <=10 (mutation present/absent) if needed
col_tot = ct.sum(axis=0)
keep_cols = [c for c in ct.columns if col_tot[c] > 10]
ct2 = ct[keep_cols]

# If after filtering we don't have at least 2 columns and 2 rows, can't compute meaningful chi-square
chi2 = None
if ct2.shape[0] >= 2 and ct2.shape[1] >= 2:
    obs = ct2.to_numpy(dtype=float)
    row_tot = obs.sum(axis=1, keepdims=True)
    col_tot2 = obs.sum(axis=0, keepdims=True)
    grand = obs.sum()
    exp = row_tot @ (col_tot2 / grand)
    chi2 = float(((obs - exp)**2 / exp).sum())

out = {
    'n_patients_used': int(df.shape[0]),
    'contingency_table_after_filter': ct2.reset_index().to_dict(orient='records'),
    'chi_square_statistic': chi2,
    'rows_histology_categories': int(ct2.shape[0]),
    'cols_mut_status_categories': int(ct2.shape[1]),
    'col_totals': {str(k): int(v) for k,v in ct2.sum(axis=0).to_dict().items()},
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dGqGzP3NQBexBimZHNt0AeZD': 'file_storage/call_dGqGzP3NQBexBimZHNt0AeZD.json', 'var_call_x9SnihkH33ZTMveaBWIKrplS': ['clinical_info'], 'var_call_ENNbtfsGSlCmhnFDCYVuMabK': [{'column_name': 'Patient_description'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}], 'var_call_uexcWgoRgZsWgkVJDVymzBA5': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}], 'var_call_GGfce5XJn3h5mdDtwrRvDg4f': [], 'var_call_vLqeG8CRcLtUBtidNKUL8erq': [], 'var_call_tCdhIxQItKejRqdxCyO3vEgg': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_l6XdWsYUYTEmxVdOAQunSLpY': [{'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_P17U7fLhQQujtLUkI1qhzYN2': 'file_storage/call_P17U7fLhQQujtLUkI1qhzYN2.json'}

exec(code, env_args)
