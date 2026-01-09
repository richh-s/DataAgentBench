code = """import json, re, pandas as pd

# Load clinical histology (BRCA cohort inferred from ICD10 C50; female parsed from Patient_description)
path_clin = var_call_tREYuBfSBh6boibHLTOH7ozc
with open(path_clin, 'r') as f:
    clin = json.load(f)

df_clin = pd.DataFrame(clin)
# extract TCGA barcode and sex from free-text Patient_description
df_clin['tcga_barcode'] = df_clin['participant_barcode'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
df_clin['sex'] = df_clin['participant_barcode'].str.extract(r'\b(FEMALE|MALE)\b', expand=False)
# keep only female and with a valid barcode
df_clin = df_clin[(df_clin['sex']=='FEMALE') & df_clin['tcga_barcode'].notna()].copy()
# normalize histology
_dfh = df_clin['histological_type'].astype(str).str.strip()
_dfh = _dfh.str.replace(r'\s+', ' ', regex=True)
df_clin['histology'] = _dfh

# Load CDH1 PASS mutations (dedupe by participant)
path_mut = var_call_mIYnBSmXfxEk5Pt6XoyR78sK
with open(path_mut, 'r') as f:
    mut = json.load(f)
df_mut = pd.DataFrame(mut)
df_mut = df_mut[['participant_barcode']].dropna()
df_mut['tcga_barcode'] = df_mut['participant_barcode'].astype(str).str.strip()
df_mut = df_mut.drop_duplicates('tcga_barcode')
df_mut['CDH1_mut'] = 1

# Merge
m = df_clin[['tcga_barcode','histology']].drop_duplicates('tcga_barcode').merge(df_mut[['tcga_barcode','CDH1_mut']], on='tcga_barcode', how='left')
m['CDH1_mut'] = m['CDH1_mut'].fillna(0).astype(int)

# Build contingency by histology x mutation
ct = pd.crosstab(m['histology'], m['CDH1_mut'])
# Ensure both columns 0 and 1 exist
for col in [0,1]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[0,1]]
ct.columns = ['no_mut','mut']

# Exclude categories with marginal totals <=10 (row totals)
ct['row_total'] = ct.sum(axis=1)
ct_f = ct[ct['row_total']>10].copy()
# Also ensure column totals >10? question says categories with marginal totals <=10; apply to rows only.

obs = ct_f[['no_mut','mut']].to_numpy(dtype=float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ (col_tot / grand)
chi2 = float(((obs-exp)**2/exp).sum()) if grand>0 else None

dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

# prepare compact output including table
out = {
    'chi_square_statistic': chi2,
    'degrees_of_freedom': dof,
    'grand_total_n': int(grand),
    'included_histology_categories': int(obs.shape[0]),
    'contingency_table': ct_f[['no_mut','mut']].astype(int).reset_index().rename(columns={'histology':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mIYnBSmXfxEk5Pt6XoyR78sK': 'file_storage/call_mIYnBSmXfxEk5Pt6XoyR78sK.json', 'var_call_3P6VEQhYjzAlvk3YFEJzXB15': ['clinical_info'], 'var_call_W1WyhivEpUupxR1ejrFqBejh': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_tREYuBfSBh6boibHLTOH7ozc': 'file_storage/call_tREYuBfSBh6boibHLTOH7ozc.json'}

exec(code, env_args)
