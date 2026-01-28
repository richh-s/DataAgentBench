code = """import json
import pandas as pd
# load clinical BRCA subset from earlier file
clin_path = var_call_1AtI4DXBpEk51HUqYoXpm9qH
with open(clin_path,'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)
# extract barcode
import re
clin_df['patient_barcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
# keep only FEMALE entries (Patient_description contains FEMALE already in query)
# Keep only rows with known histological_type not null or '[Not Available]'
clin_df = clin_df[~clin_df['histological_type'].isna()]
# standardize histological types
clin_df['histological_type_clean'] = clin_df['histological_type'].str.strip()
# load mutation data
muts_path = var_call_IdX4pu1dZFxhAQNxZisazP84
with open(muts_path,'r') as f:
    muts = json.load(f)
muts_df = pd.DataFrame(muts)
muts_df['patient_barcode'] = muts_df['ParticipantBarcode'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
# only PASS already
muts_df = muts_df[muts_df['FILTER']=='PASS']
# create mutation presence flag per patient
mutant = muts_df[['patient_barcode']].drop_duplicates()
mutant['CDH1_mutation'] = 'Mutant'
# merge with clinical
merged = pd.merge(clin_df[['patient_barcode','histological_type_clean']], mutant, on='patient_barcode', how='left')
merged['CDH1_mutation'] = merged['CDH1_mutation'].fillna('Wildtype')
# count table
ct = merged.groupby(['histological_type_clean','CDH1_mutation']).size().unstack(fill_value=0)
# exclude hist types with marginal totals <=10
ct['total'] = ct.sum(axis=1)
ct_filtered = ct[ct['total']>10]
# compute chi-square statistic manually
ct2 = ct_filtered[['Mutant','Wildtype']].astype(int)
row_totals = ct2.sum(axis=1)
col_totals = ct2.sum(axis=0)
grand_total = row_totals.sum()
expected = pd.DataFrame(index=ct2.index, columns=ct2.columns)
chi2 = 0.0
for r in ct2.index:
    for c in ct2.columns:
        E = (row_totals[r]*col_totals[c])/grand_total if grand_total>0 else 0
        O = ct2.loc[r,c]
        if E>0:
            chi2 += (O - E)**2 / E
        expected.loc[r,c] = E
# prepare outputs
out = {
    'contingency_table_filtered': ct2.reset_index().to_dict(orient='records'),
    'expected_table': expected.reset_index().fillna(0).to_dict(orient='records'),
    'row_totals': row_totals.to_dict(),
    'col_totals': col_totals.to_dict(),
    'grand_total': int(grand_total),
    'chi_square': float(chi2)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_95WKTNPbhY7qGYbk2R3rqwM6': ['clinical_info'], 'var_call_rAAyGm642Nicn9GPSJRzqfXt': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_6LY7eSsWc2dNB4pC44U1fNw6': 'file_storage/call_6LY7eSsWc2dNB4pC44U1fNw6.json', 'var_call_8RbdqjyY01Dzgfo4DF61Xu9U': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'sample_values': {'Patient_description': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'], 'histological_type': ['Serous Cystadenocarcinoma'], 'tumor_tissue_site': ['Ovary']}}, 'var_call_1AtI4DXBpEk51HUqYoXpm9qH': 'file_storage/call_1AtI4DXBpEk51HUqYoXpm9qH.json', 'var_call_G6hcZjx9qCAKBph7widASsqR': {'n_records': 200, 'unique_hist_types': 8, 'hist_counts_sample': {'Infiltrating Ductal Carcinoma': 136, 'Infiltrating Lobular Carcinoma': 43, 'Other  specify': 11, 'Mucinous Carcinoma': 4, 'Metaplastic Carcinoma': 3, 'Infiltrating Carcinoma NOS': 1, 'Medullary Carcinoma': 1, 'Mixed Histology (please specify)': 1}}, 'var_call_IdX4pu1dZFxhAQNxZisazP84': 'file_storage/call_IdX4pu1dZFxhAQNxZisazP84.json', 'var_call_4U8m0aFIzJSHXfmgtBBQdoKL': {'n_cdh1_mutant_patients': 247}}

exec(code, env_args)
