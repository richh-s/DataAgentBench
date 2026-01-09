code = """import json, re, pandas as pd

# Load clinical records
path = var_call_C4cVMtfGPO6OHYqt95dnuJC9
with open(path, 'r') as f:
    clinical = json.load(f)

def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

cl_df = pd.DataFrame(clinical)
# normalize key name (came back lowercased in preview)
if 'participantbarcode' in cl_df.columns and 'ParticipantBarcode' not in cl_df.columns:
    cl_df = cl_df.rename(columns={'participantbarcode':'ParticipantBarcode'})

cl_df['ParticipantBarcode'] = cl_df['ParticipantBarcode'].map(extract_barcode)
cl_df = cl_df.dropna(subset=['ParticipantBarcode','histological_type'])
cl_df['histological_type'] = cl_df['histological_type'].astype(str).str.strip()
cl_df = cl_df[cl_df['histological_type'].str.len() > 0]

# female only (from Patient_description text)
cl_df = cl_df[cl_df['ParticipantBarcode'].notna()]
# We know these are Breast invasive carcinoma but include a safety female filter from original text
# Use the original text to identify female
orig_text = pd.DataFrame(clinical)
if 'participantbarcode' in orig_text.columns and 'ParticipantBarcode' not in orig_text.columns:
    orig_text = orig_text.rename(columns={'participantbarcode':'ParticipantBarcode'})
orig_text['barcode'] = orig_text['ParticipantBarcode'].map(extract_barcode)
orig_text['is_female'] = orig_text['ParticipantBarcode'].astype(str).str.contains('FEMALE', case=False, na=False)
sex_map = orig_text.dropna(subset=['barcode']).drop_duplicates('barcode')[['barcode','is_female']]
cl_df = cl_df.merge(sex_map, left_on='ParticipantBarcode', right_on='barcode', how='left')
cl_df = cl_df[cl_df['is_female'] == True]
cl_df = cl_df[['ParticipantBarcode','histological_type']].drop_duplicates()

# Load mutations (CDH1 PASS)
mut_path = var_call_I8vJoZoYr2DskRWuB6puV5dI
with open(mut_path, 'r') as f:
    muts = json.load(f)
mut_df = pd.DataFrame(muts)
mut_barcodes = set(mut_df['ParticipantBarcode'].dropna().astype(str).unique())

cl_df['CDH1_mut'] = cl_df['ParticipantBarcode'].isin(mut_barcodes)

# contingency by histological type
ct = pd.crosstab(cl_df['histological_type'], cl_df['CDH1_mut'])
# ensure both columns
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]
ct.columns = ['CDH1_WT','CDH1_MUT']

# Exclude categories with marginal totals <=10 (row totals)
ct['row_total'] = ct.sum(axis=1)
ct_filt = ct[ct['row_total'] > 10].drop(columns=['row_total'])

# Also ensure column totals >10? prompt says categories with marginal totals <=10; apply to rows.
obs = ct_filt[['CDH1_WT','CDH1_MUT']].to_numpy()
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ (col_tot / grand)
chi2 = float(((obs - exp)**2 / exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

result = {
    'chi_square': chi2,
    'degrees_of_freedom': dof,
    'grand_total_n': int(grand),
    'column_totals': {'CDH1_WT': int(col_tot[0,0]), 'CDH1_MUT': int(col_tot[0,1])},
    'included_histological_types': ct_filt.reset_index().to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_I8vJoZoYr2DskRWuB6puV5dI': 'file_storage/call_I8vJoZoYr2DskRWuB6puV5dI.json', 'var_call_DDj5vZuOBpxCGAj7upg7EXHX': ['clinical_info'], 'var_call_E9Zxg9PoHkAaEt7HieSuYfST': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_ANrVtyAC2Wu01tSyxbWadg8q': [], 'var_call_DQMpX6FRk4Sh87dyK6SuWqMc': [], 'var_call_kXWWW6EQ62kOe76pgg4zR3h6': [{'participantbarcode': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participantbarcode': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participantbarcode': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participantbarcode': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participantbarcode': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_call_C4cVMtfGPO6OHYqt95dnuJC9': 'file_storage/call_C4cVMtfGPO6OHYqt95dnuJC9.json'}

exec(code, env_args)
