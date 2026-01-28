code = """import json, re, pandas as pd

# Load clinical histological types for breast (ICD10 C50*)
clin_src = var_call_QJNyL8wunf9Pe0uPqXfykWfp
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

df_clin = pd.DataFrame(clin)
# normalize column name (came back lowercased)
if 'participantbarcode' in df_clin.columns and 'ParticipantBarcode' not in df_clin.columns:
    df_clin = df_clin.rename(columns={'participantbarcode':'ParticipantBarcode'})

def extract_tcga_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

df_clin['ParticipantBarcode'] = df_clin['ParticipantBarcode'].map(extract_tcga_barcode)
# keep known barcodes and histology
df_clin = df_clin[df_clin['ParticipantBarcode'].notna() & df_clin['histological_type'].notna()].copy()

# Restrict to female by parsing Patient_description text
# (gender column not present); use regex ' a FEMALE ' etc.
def is_female(desc):
    if desc is None:
        return False
    s = str(desc).upper()
    return ' FEMALE' in s and ' MALE' not in s

df_clin = df_clin[df_clin.apply(lambda r: is_female(r.get('ParticipantBarcode_raw', None)), axis=1) if 'ParticipantBarcode_raw' in df_clin.columns else df_clin.index.map(lambda i: True)]
# above likely no raw col; instead re-read from original Patient_description
# reconstruct raw description from clin list
raw_map = {extract_tcga_barcode(r.get('participantbarcode') or r.get('ParticipantBarcode')): (r.get('participantbarcode') or r.get('ParticipantBarcode')) for r in clin}
df_clin['raw_desc'] = df_clin['ParticipantBarcode'].map(raw_map)
df_clin = df_clin[df_clin['raw_desc'].map(is_female)].copy()

# Deduplicate to one histology per patient
# if multiple, take first
hist_by_pt = df_clin.groupby('ParticipantBarcode', as_index=False).agg({'histological_type':'first'})

# Load mutation PASS entries for CDH1
mut_src = var_call_mvcmTHU4PrPAdvLcClgkPuf4
if isinstance(mut_src, str):
    with open(mut_src, 'r') as f:
        mut = json.load(f)
else:
    mut = mut_src

df_mut = pd.DataFrame(mut)
mut_pts = set(df_mut['ParticipantBarcode'].dropna().unique().tolist())

# Merge and create mutation presence
hist_by_pt['CDH1_mut'] = hist_by_pt['ParticipantBarcode'].isin(mut_pts).astype(int)

# Build contingency table
ct = pd.crosstab(hist_by_pt['histological_type'], hist_by_pt['CDH1_mut'])
# ensure both columns 0 and 1 exist
for c in [0,1]:
    if c not in ct.columns:
        ct[c]=0
ct = ct[[0,1]]

# Exclude categories with marginal totals <= 10 (row totals)
row_tot = ct.sum(axis=1)
ct_f = ct[row_tot > 10].copy()

# Also exclude columns with marginal totals <=10
col_tot = ct_f.sum(axis=0)
keep_cols = [c for c in ct_f.columns if col_tot[c] > 10]
ct_f = ct_f[keep_cols]

# Compute chi-square
import numpy as np
O = ct_f.values.astype(float)
rt = O.sum(axis=1, keepdims=True)
ctot = O.sum(axis=0, keepdims=True)
N = O.sum()
E = rt @ ctot / N if N>0 else O
chi2 = float(((O-E)**2 / E).sum()) if N>0 else None

a = {
    'chi_square': chi2,
    'grand_total': int(N),
    'rows_kept': ct_f.index.tolist(),
    'cols_kept': [str(c) for c in ct_f.columns.tolist()],
    'contingency_table': [{
        'histological_type': idx,
        **{str(c): int(ct_f.loc[idx, c]) for c in ct_f.columns}
    } for idx in ct_f.index]
}

print('__RESULT__:')
print(json.dumps(a))"""

env_args = {'var_call_mvcmTHU4PrPAdvLcClgkPuf4': 'file_storage/call_mvcmTHU4PrPAdvLcClgkPuf4.json', 'var_call_FdsDfT1U4QLsiMuKjCIDMeH2': ['clinical_info'], 'var_call_vKKN8hwtwvjruFYk51hTrD1b': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_v2Acas8nxT3Bof0RcM96izoy': [], 'var_call_QJNyL8wunf9Pe0uPqXfykWfp': 'file_storage/call_QJNyL8wunf9Pe0uPqXfykWfp.json'}

exec(code, env_args)
