code = """import json, re, pandas as pd

# load clinical
p = var_call_kDOQqYv9FaxmOqvKtobkuEwt
with open(p, 'r') as f:
    clinical = json.load(f)

df_c = pd.DataFrame(clinical)
# normalize key casing
if 'participantbarcode' in df_c.columns and 'ParticipantBarcode' not in df_c.columns:
    df_c = df_c.rename(columns={'participantbarcode':'ParticipantBarcode'})

# extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_c['ParticipantBarcode_extracted'] = df_c['ParticipantBarcode'].astype(str).str.extract(pat, expand=False)
# extract sex from text; keep only FEMALE
sex = df_c['ParticipantBarcode'].astype(str).str.extract(r'\b(FEMALE|MALE)\b', expand=False)
df_c['sex'] = sex

df_c = df_c[df_c['sex']=='FEMALE'].copy()
df_c = df_c[df_c['ParticipantBarcode_extracted'].notna()].copy()
df_c = df_c[['ParticipantBarcode_extracted','histological_type']].rename(columns={'ParticipantBarcode_extracted':'ParticipantBarcode'})

# mutation list
mpath = var_call_ZcenyRU4tgu8fBsMg8YIbyoT
with open(mpath,'r') as f:
    muts = json.load(f)
df_m = pd.DataFrame(muts)
# patient-level mutated flag (PASS already filtered)
df_m = df_m.dropna(subset=['ParticipantBarcode'])
mut_set = set(df_m['ParticipantBarcode'].astype(str).unique())

# join and contingency
c = df_c.dropna(subset=['histological_type']).copy()
c['CDH1_mut'] = c['ParticipantBarcode'].astype(str).isin(mut_set).astype(int)

# build contingency table
ct = pd.crosstab(c['histological_type'], c['CDH1_mut'])
# ensure both columns 0 and 1 exist
for col in [0,1]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[0,1]]
ct.columns = ['WT','MUT']

# exclude categories (rows) with marginal totals <=10
ct['row_total']=ct.sum(axis=1)
ct_f = ct[ct['row_total']>10].drop(columns=['row_total'])

# compute chi-square
obs = ct_f[['WT','MUT']].astype(float)
row_tot = obs.sum(axis=1)
col_tot = obs.sum(axis=0)
grand = obs.values.sum()
exp = pd.DataFrame({
    'WT': row_tot * col_tot['WT'] / grand,
    'MUT': row_tot * col_tot['MUT'] / grand
})
chi2 = ((obs-exp)**2/exp).to_numpy().sum()

df_res = {
    'chi_square': float(chi2),
    'grand_total': int(grand),
    'row_categories_used': int(obs.shape[0]),
    'contingency_table': obs.astype(int).reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(df_res))"""

env_args = {'var_call_ZcenyRU4tgu8fBsMg8YIbyoT': 'file_storage/call_ZcenyRU4tgu8fBsMg8YIbyoT.json', 'var_call_Lf8yXUWnYNChTcj0aNaU4WbW': ['clinical_info'], 'var_call_87QtouVkICtFiMuB88CJFemc': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_Jah7XTQpPfEQjfeATj3y9YTS': [{'n_total': '1089', 'n_hist': '1087'}], 'var_call_kDOQqYv9FaxmOqvKtobkuEwt': 'file_storage/call_kDOQqYv9FaxmOqvKtobkuEwt.json'}

exec(code, env_args)
