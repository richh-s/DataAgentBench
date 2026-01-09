code = """import json, re, pandas as pd

# Load clinical BRCA (icd_10 C50.9) with known histological_type
p = var_call_RtiUhn9rZoYsmZr7syqPXCw4
if isinstance(p, str):
    with open(p, 'r') as f:
        clin = json.load(f)
else:
    clin = p

# Extract TCGA barcode from Patient_description text
rows = []
for r in clin:
    desc = r.get('participant_barcode')
    hist = r.get('histological_type')
    if not desc or not hist:
        continue
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m:
        continue
    rows.append({'participant_barcode': m.group(1), 'histological_type': hist.strip()})

clin_df = pd.DataFrame(rows).drop_duplicates(subset=['participant_barcode'])

# Load CDH1 mutation carriers (PASS only)
mp = var_call_tamwmoYOS9kkU2HE8QvYOsn4
if isinstance(mp, str):
    with open(mp, 'r') as f:
        muts = json.load(f)
else:
    muts = mp
mut_set = set([r['participant_barcode'] for r in muts if r.get('participant_barcode')])

clin_df['cdh1_mut'] = clin_df['participant_barcode'].isin(mut_set)

# Contingency table: histological_type x mutation
ct = pd.crosstab(clin_df['histological_type'], clin_df['cdh1_mut'])
# Ensure both columns exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]
ct.columns = ['No_MUT', 'MUT']

# Exclude categories with marginal totals <= 10 (row totals)
row_totals = ct.sum(axis=1)
ct_f = ct.loc[row_totals > 10].copy()

# Also exclude if any column marginal <= 10 after row filtering? (instruction says categories; apply to rows)

# Compute chi-square statistic
O = ct_f.values.astype(float)
row_sums = O.sum(axis=1, keepdims=True)
col_sums = O.sum(axis=0, keepdims=True)
grand = O.sum()
E = row_sums @ (col_sums / grand)
chi2 = float(((O - E)**2 / E).sum())

df = int((ct_f.shape[0]-1)*(ct_f.shape[1]-1))

out = {
    'chi_square': chi2,
    'degrees_of_freedom': df,
    'grand_total': int(grand),
    'table_used': ct_f.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tamwmoYOS9kkU2HE8QvYOsn4': 'file_storage/call_tamwmoYOS9kkU2HE8QvYOsn4.json', 'var_call_R5XdXc9CTq0MUfUCJr09lSAN': ['clinical_info'], 'var_call_92lyZI7LPlq3n3x4zH7IEupw': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_hOBCvUMGPP0zKAuKraxwNTK9': [], 'var_call_TuNJdoEQw7TgAhDSteiQ9XOe': [{'tissue_source_site': 'AA', 'n': '164'}, {'tissue_source_site': '06', 'n': '153'}, {'tissue_source_site': 'DD', 'n': '151'}, {'tissue_source_site': 'BH', 'n': '149'}, {'tissue_source_site': 'BR', 'n': '138'}, {'tissue_source_site': 'CV', 'n': '135'}, {'tissue_source_site': 'BP', 'n': '130'}, {'tissue_source_site': 'DX', 'n': '120'}, {'tissue_source_site': '13', 'n': '111'}, {'tissue_source_site': 'B0', 'n': '107'}, {'tissue_source_site': 'HT', 'n': '103'}, {'tissue_source_site': 'A2', 'n': '102'}, {'tissue_source_site': '24', 'n': '99'}, {'tissue_source_site': 'EJ', 'n': '96'}, {'tissue_source_site': 'EE', 'n': '95'}, {'tissue_source_site': '02', 'n': '92'}, {'tissue_source_site': 'DJ', 'n': '91'}, {'tissue_source_site': '55', 'n': '91'}, {'tissue_source_site': 'E2', 'n': '90'}, {'tissue_source_site': 'DU', 'n': '86'}], 'var_call_DIZLB961xn7rzfI8W3Ld8jwB': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_u7A7nrwiKb52qNssdJKYRFXg': [{'icd_10': 'C50.9', 'n': '1078'}, {'icd_10': 'C71.9', 'n': '646'}, {'icd_10': 'C64.9', 'n': '585'}, {'icd_10': 'C56.9', 'n': '579'}, {'icd_10': 'C34.1', 'n': '560'}, {'icd_10': 'C54.1', 'n': '551'}, {'icd_10': 'C73', 'n': '503'}, {'icd_10': 'C61', 'n': '494'}, {'icd_10': 'C71.0', 'n': '438'}, {'icd_10': 'C22.0', 'n': '376'}, {'icd_10': 'C34.3', 'n': '342'}, {'icd_10': 'C53.9', 'n': '300'}, {'icd_10': 'C64.1', 'n': '286'}, {'icd_10': 'C67.9', 'n': '237'}, {'icd_10': 'C16.3', 'n': '156'}, {'icd_10': 'C74.9', 'n': '145'}, {'icd_10': 'C25.0', 'n': '140'}, {'icd_10': 'C02.9', 'n': '129'}, {'icd_10': 'C15.5', 'n': '122'}, {'icd_10': 'C32.9', 'n': '118'}, {'icd_10': 'C48.0', 'n': '116'}, {'icd_10': 'C16.0', 'n': '112'}, {'icd_10': 'C18.7', 'n': '107'}, {'icd_10': 'C18.2', 'n': '102'}, {'icd_10': 'C16.2', 'n': '101'}, {'icd_10': 'C18.9', 'n': '98'}, {'icd_10': 'C74.0', 'n': '93'}, {'icd_10': 'C77.3', 'n': '92'}, {'icd_10': 'C37', 'n': '85'}, {'icd_10': 'C45.0', 'n': '85'}], 'var_call_RtiUhn9rZoYsmZr7syqPXCw4': 'file_storage/call_RtiUhn9rZoYsmZr7syqPXCw4.json'}

exec(code, env_args)
