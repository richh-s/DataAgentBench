code = """import json, re, pandas as pd

# load clinical
path_clin = var_call_bd3yj5CzopYnmbzDjRlJPdXk
with open(path_clin,'r') as f:
    clin = json.load(f)
df_clin = pd.DataFrame(clin)

def extract_tcga_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

df_clin['barcode'] = df_clin['participant_barcode'].map(extract_tcga_barcode)
df_clin = df_clin.dropna(subset=['barcode','histological_type'])
# only females implied by text; enforce by filtering string contains 'FEMALE'
df_clin = df_clin[df_clin['participant_barcode'].str.contains('FEMALE', na=False)]

df_mut_path = var_call_rzkv9AVXm8tUEtlQumgkpNMR
with open(df_mut_path,'r') as f:
    mut = json.load(f)
df_mut = pd.DataFrame(mut)
# unique mutated participants
mutated = set(df_mut['participant_barcode'].dropna().unique().tolist())

# build dataset of BRCA females with hist type
# BRCA selection by icd_10 C50 already

df = df_clin[['barcode','histological_type']].drop_duplicates('barcode')
df['CDH1_mut'] = df['barcode'].isin(mutated).astype(int)

# contingency table
ct = pd.crosstab(df['histological_type'], df['CDH1_mut'])
# ensure both columns 0 and 1 exist
for c in [0,1]:
    if c not in ct.columns:
        ct[c]=0
ct = ct[[0,1]]

# exclude categories with marginal totals <=10 (row totals)
ct['row_total'] = ct.sum(axis=1)
ct_f = ct[ct['row_total']>10].drop(columns=['row_total'])

# also ensure column totals >10? question says categories with marginal totals <=10 (likely rows). apply to columns too
col_totals = ct_f.sum(axis=0)
cols_keep = [c for c in ct_f.columns if col_totals[c]>10]
ct_f = ct_f[cols_keep]

# compute chi-square
import numpy as np
O = ct_f.to_numpy(dtype=float)
row_tot = O.sum(axis=1, keepdims=True)
col_tot = O.sum(axis=0, keepdims=True)
N = O.sum()
E = row_tot @ (col_tot / N)
chi2 = float(((O-E)**2 / E).sum()) if N>0 else None

deg_freedom = int((O.shape[0]-1)*(O.shape[1]-1)) if O.shape[0]>0 and O.shape[1]>0 else 0

result = {
    'chi_square': chi2,
    'degrees_of_freedom': deg_freedom,
    'n_patients_used': int(df.shape[0]),
    'n_hist_types_after_filter': int(ct_f.shape[0]),
    'contingency_table': ct_f.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rzkv9AVXm8tUEtlQumgkpNMR': 'file_storage/call_rzkv9AVXm8tUEtlQumgkpNMR.json', 'var_call_ZZS1TGbMJZSBZKrvQIecDc4h': ['clinical_info'], 'var_call_j9JbX6jtl0tj2lr5uyTzE2nn': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_bd3yj5CzopYnmbzDjRlJPdXk': 'file_storage/call_bd3yj5CzopYnmbzDjRlJPdXk.json'}

exec(code, env_args)
