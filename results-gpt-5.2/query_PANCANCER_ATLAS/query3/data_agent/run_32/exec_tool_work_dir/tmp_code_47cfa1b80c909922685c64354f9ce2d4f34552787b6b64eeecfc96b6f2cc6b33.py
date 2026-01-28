code = """import json, re, pandas as pd

# Load clinical records (may be file path)
clin_src = var_call_QBeuWJB2N5EFJtS4ZT9g1pPw
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

mut_src = var_call_Vl1Ok8AAGUGA4TsH4VobTHZU
if isinstance(mut_src, str):
    with open(mut_src, 'r') as f:
        mut = json.load(f)
else:
    mut = mut_src

# Extract TCGA barcode from Patient_description text
rows=[]
for r in clin:
    pdsc = r.get('participant_barcode')
    ht = r.get('histological_type')
    if not pdsc or not ht:
        continue
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', pdsc)
    if not m:
        continue
    rows.append({'participant_barcode': m.group(1), 'histological_type': ht.strip()})

clin_df = pd.DataFrame(rows).drop_duplicates(subset=['participant_barcode'])

mut_df = pd.DataFrame(mut).drop_duplicates()
mut_set = set(mut_df['participant_barcode'].dropna().astype(str))

clin_df['cdh1_mut'] = clin_df['participant_barcode'].isin(mut_set)

# contingency table
ct = pd.crosstab(clin_df['histological_type'], clin_df['cdh1_mut'])
# ensure both columns present
for col in [False, True]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[False, True]]

# Exclude categories with row totals <=10
ct = ct.loc[ct.sum(axis=1) > 10].copy()

# Also exclude mutation columns if marginal totals <=10
col_tot = ct.sum(axis=0)
keep_cols = [c for c in ct.columns if col_tot[c] > 10]
ct_f = ct[keep_cols].copy()

# If after filtering fewer than 2 columns or fewer than 2 rows, cannot compute chi-square association
result = {}
if ct_f.shape[0] < 2 or ct_f.shape[1] < 2:
    result = {
        'error': 'Insufficient categories after filtering to compute chi-square',
        'n_patients_with_known_histology': int(clin_df.shape[0]),
        'contingency_after_row_filter': ct.to_dict(),
        'col_totals_after_row_filter': {str(k): int(v) for k,v in col_tot.items()},
        'kept_columns': [str(c) for c in keep_cols]
    }
else:
    obs = ct_f.values.astype(float)
    row_totals = obs.sum(axis=1, keepdims=True)
    col_totals = obs.sum(axis=0, keepdims=True)
    grand = obs.sum()
    exp = row_totals @ col_totals / grand
    chi2 = float(((obs-exp)**2/exp).sum())
    dof = int((obs.shape[0]-1)*(obs.shape[1]-1))
    result = {
        'chi_square': chi2,
        'degrees_of_freedom': dof,
        'grand_total': int(grand),
        'contingency_table_used': ct_f.reset_index().to_dict(orient='records'),
        'row_totals': {idx: int(v) for idx,v in zip(ct_f.index.tolist(), ct_f.sum(axis=1).tolist())},
        'col_totals': {str(k): int(v) for k,v in ct_f.sum(axis=0).to_dict().items()},
        'n_patients_with_known_histology': int(clin_df.shape[0]),
        'n_patients_with_cdh1_pass_mut': int(clin_df['cdh1_mut'].sum())
    }

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Vl1Ok8AAGUGA4TsH4VobTHZU': 'file_storage/call_Vl1Ok8AAGUGA4TsH4VobTHZU.json', 'var_call_FQClSrDS3QUuB6NX8SRvW71g': ['clinical_info'], 'var_call_lEKTXpDSRQw2IiRvA1fYdGT1': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_QBeuWJB2N5EFJtS4ZT9g1pPw': 'file_storage/call_QBeuWJB2N5EFJtS4ZT9g1pPw.json'}

exec(code, env_args)
