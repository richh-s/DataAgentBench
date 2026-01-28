code = """import json, re, pandas as pd

# Load clinical records
clin_src = var_call_ZYUD6UzhTVTBKHqDfBubL71I
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# Load mutation carriers for CDH1 (PASS)
mut_src = var_call_3BMbeMbERJuccrNuh2l4OhbI
if isinstance(mut_src, str):
    with open(mut_src, 'r') as f:
        mut = json.load(f)
else:
    mut = mut_src

mut_set = set([r['ParticipantBarcode'] for r in mut])

# Extract TCGA barcode from Patient_description
pat = []
for r in clin:
    desc = r.get('patient_description') or r.get('Patient_description') or ''
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m:
        continue
    bc = m.group(1)
    ht = r.get('histological_type')
    if ht is None:
        continue
    ht = str(ht).strip()
    if ht == '':
        continue
    pat.append({'ParticipantBarcode': bc, 'histological_type': ht, 'has_cdh1_mut': 1 if bc in mut_set else 0})

df = pd.DataFrame(pat).drop_duplicates(subset=['ParticipantBarcode'])

# contingency
ct = pd.crosstab(df['histological_type'], df['has_cdh1_mut'])
# ensure both columns 0 and 1
for c in [0,1]:
    if c not in ct.columns:
        ct[c]=0
ct = ct[[0,1]]

# Exclude categories with marginal totals <=10 (row totals)
row_tot = ct.sum(axis=1)
ct_f = ct.loc[row_tot>10].copy()

# Also exclude if any column marginal total <=10? prompt says categories with marginal totals <=10; interpret for both rows and columns
col_tot = ct_f.sum(axis=0)
keep_cols = [c for c in ct_f.columns if col_tot[c]>10]
ct_f = ct_f[keep_cols]

# If after filtering only one column, chi-square not defined
result = {}
if ct_f.shape[0] < 2 or ct_f.shape[1] < 2:
    result = {
        'error': 'Not enough categories after filtering to compute chi-square.',
        'n_patients': int(df.shape[0]),
        'n_histology_categories_before_filter': int(ct.shape[0]),
        'n_histology_categories_after_filter': int(ct_f.shape[0]),
        'column_totals_after_filter': {str(k): int(v) for k,v in ct_f.sum(axis=0).to_dict().items()},
    }
else:
    grand = ct_f.values.sum()
    row_tot = ct_f.sum(axis=1).values.reshape(-1,1)
    col_tot = ct_f.sum(axis=0).values.reshape(1,-1)
    expected = row_tot.dot(col_tot)/grand
    observed = ct_f.values.astype(float)
    chi2 = float(((observed-expected)**2/expected).sum())
    dof = int((ct_f.shape[0]-1)*(ct_f.shape[1]-1))
    result = {
        'chi_square_statistic': chi2,
        'degrees_of_freedom': dof,
        'n_patients_used': int(grand),
        'histology_categories_used': [str(x) for x in ct_f.index.tolist()],
        'contingency_table': {
            str(idx): {str(col): int(ct_f.loc[idx, col]) for col in ct_f.columns}
            for idx in ct_f.index
        },
        'row_totals': {str(idx): int(ct_f.loc[idx].sum()) for idx in ct_f.index},
        'column_totals': {str(col): int(ct_f[col].sum()) for col in ct_f.columns},
        'excluded_histology_categories_row_total_le_10': [str(i) for i in ct.index[row_tot.ctypes.data==row_tot.ctypes.data] ]
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3BMbeMbERJuccrNuh2l4OhbI': 'file_storage/call_3BMbeMbERJuccrNuh2l4OhbI.json', 'var_call_ntpY9D88UmDy93Dt2zEgEeX6': ['clinical_info'], 'var_call_AVe2PZAVo3EWJUULFit5Lz8m': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_ivshstKPSUqk3cOMHzInev1w': [{'participantbarcode': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participantbarcode': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participantbarcode': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participantbarcode': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'participantbarcode': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_ZYUD6UzhTVTBKHqDfBubL71I': 'file_storage/call_ZYUD6UzhTVTBKHqDfBubL71I.json'}

exec(code, env_args)
