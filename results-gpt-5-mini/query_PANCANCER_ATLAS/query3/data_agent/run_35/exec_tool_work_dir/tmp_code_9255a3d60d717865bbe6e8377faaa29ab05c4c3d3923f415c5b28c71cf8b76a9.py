code = """import pandas as pd
import json

clinical_path = var_call_CpER4D8kxe0emTc45fgMCaUH

df = pd.read_json(clinical_path)

# list all columns
cols = list(df.columns)
# search for any cell containing 'BRCA' or 'Breast' anywhere (case-insensitive), limit results
mask_br = df.apply(lambda col: col.astype(str).str.contains('BRCA', case=False, na=False).any())
mask_breast = df.apply(lambda col: col.astype(str).str.contains('breast', case=False, na=False).any())

cols_with_br = [c for c,v in mask_br.items() if v]
cols_with_breast = [c for c,v in mask_breast.items() if v]

# also show unique values of likely columns
sample_values = {}
for c in cols[:200]:
    try:
        sample_values[c] = df[c].dropna().astype(str).unique()[:10].tolist()
    except Exception as e:
        sample_values[c] = ['error']

out = {'n_rows': int(df.shape[0]), 'n_cols': int(df.shape[1]), 'columns': cols, 'cols_with_BRCA': cols_with_br, 'cols_with_breast': cols_with_breast, 'sample_values_first_cols': {k: sample_values[k] for k in cols[:40]}}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WUTduE6YXwIB0XzZJkiicgTn': ['clinical_info'], 'var_call_raxK4sfkMMSuTsT8liLto0mB': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CpER4D8kxe0emTc45fgMCaUH': 'file_storage/call_CpER4D8kxe0emTc45fgMCaUH.json', 'var_call_hk8JPyVKGwxzlQ9AneWjnDX9': 'file_storage/call_hk8JPyVKGwxzlQ9AneWjnDX9.json', 'var_call_ES3df2b95r7I6fmF0q6V63mX': {'clin_rows': 200, 'mut_rows': 261, 'clin_columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight'], 'mut_columns': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'pd_sample': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'], 'barcode_sample': ['TCGA-31-1953', 'TCGA-36-1576', 'TCGA-25-2408', 'TCGA-29-2427', 'TCGA-10-0933', 'TCGA-23-1124', 'TCGA-23-2641', 'TCGA-23-1118', 'TCGA-23-1120', 'TCGA-23-2081'], 'barcode_nulls': 0, 'hist_unique_sample': ['Serous Cystadenocarcinoma', 'Treated primary GBM', 'Untreated primary (de novo) GBM', 'Leiomyosarcoma (LMS)'], 'mask_breast_count': 0, 'mask_female_count': 193, 'both_mask_count': 0, 'mask_hist_known_count': 200, 'df_brca_female_count': 0, 'df_brca_female_sample_pd': [], 'df_brca_female_sample_hist': [], 'df_brca_female_barcodes_sample': [], 'dedup_count': 0, 'mut_unique_barcodes': 247, 'intersect_barcodes_count': 0, 'ct_shape': [0, 0], 'ct_head': {}, 'ct_columns': [], 'yes_col_present': False, 'no_col_present': False, 'exception': 'cannot convert float NaN to integer'}}

exec(code, env_args)
