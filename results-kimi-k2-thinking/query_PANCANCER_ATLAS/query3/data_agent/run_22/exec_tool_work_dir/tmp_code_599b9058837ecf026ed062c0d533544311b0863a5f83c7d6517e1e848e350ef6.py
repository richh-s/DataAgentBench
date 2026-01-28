code = """import json, pandas as pd, re
import math

# Load clinical data for BRCA female patients with known histological types
clinical_file_path = locals()['var_functions.query_db:30']
with open(clinical_file_path, 'r') as f:
    clinical_data = json.load(f)

# Load all CDH1 mutation data with PASS filter
mutation_file_path = locals()['var_functions.query_db:26']
with open(mutation_file_path, 'r') as f:
    mutation_data = json.load(f)

# Convert to DataFrames
df_clinical = pd.DataFrame(clinical_data)
df_mutations = pd.DataFrame(mutation_data)

# Extract TCGA barcodes from Patient_description
def extract_barcode(description):
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', description)
    return match.group(0) if match else None

df_clinical['patient_barcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Get list of patients with CDH1 mutations
cdh1_mutated_patients = set(df_mutations['ParticipantBarcode'].unique())

# Create patient info with histological type and mutation status
patient_info = []
for idx, row in df_clinical.iterrows():
    barcode = row['patient_barcode']
    hist_type = row['histological_type']
    if barcode and hist_type and hist_type != '[Not Applicable]' and 'specify' not in str(hist_type).lower():
        has_cdh1_mutation = barcode in cdh1_mutated_patients
        patient_info.append({
            'patient_barcode': barcode,
            'histological_type': hist_type,
            'cdh1_mutation': has_cdh1_mutation
        })

df_patient = pd.DataFrame(patient_info)
print('Processed patients:', len(df_patient))
print('Patients with CDH1 mutations:', df_patient['cdh1_mutation'].sum())
print('Histological types:', df_patient['histological_type'].value_counts())

# Create contingency table
contingency = pd.crosstab(df_patient['histological_type'], df_patient['cdh1_mutation'])
contingency.columns = ['No_Mutation', 'Mutation']

print('Initial contingency table:')
print(contingency)

# Calculate marginal totals
row_totals = contingency.sum(axis=1)
col_totals = contingency.sum(axis=0)
grand_total = contingency.values.sum()

print('Row totals:', row_totals)
print('Column totals:', col_totals)
print('Grand total:', grand_total)

# Filter out categories with marginal totals <= 10
valid_hist_types = row_totals[row_totals > 10].index
contingency_filtered = contingency.loc[valid_hist_types]

print('Filtered contingency table:')
print(contingency_filtered)

result_dict = {
    'total_patients': len(df_patient),
    'cdh1_mutated_patients': df_patient['cdh1_mutation'].sum(),
    'histological_type_counts': contingency_filtered.shape[0]
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'num_records': 20, 'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'sample_patient_desc': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Tumor_SampleBarcode': 'TCGA-AR-A1AT-01A', 'Tumor_AliquotBarcode': 'TCGA-AR-A1AT-01A-11D-A12Q-09', 'Normal_SampleBarcode': 'TCGA-AR-A1AT-10A', 'Normal_AliquotBarcode': 'TCGA-AR-A1AT-10A-01D-A12Q-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.944delA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Tumor_SampleBarcode': 'TCGA-BS-A0U8-01A', 'Tumor_AliquotBarcode': 'TCGA-BS-A0U8-01A-11D-A10B-09', 'Normal_SampleBarcode': 'TCGA-BS-A0U8-10A', 'Normal_AliquotBarcode': 'TCGA-BS-A0U8-10A-01D-A10B-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.2471C>T', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Tumor_SampleBarcode': 'TCGA-D8-A27G-01A', 'Tumor_AliquotBarcode': 'TCGA-D8-A27G-01A-11D-A16D-09', 'Normal_SampleBarcode': 'TCGA-D8-A27G-10A', 'Normal_AliquotBarcode': 'TCGA-D8-A27G-10A-01D-A16D-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G169Rfs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.504dupA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Tumor_SampleBarcode': 'TCGA-E6-A1LX-01A', 'Tumor_AliquotBarcode': 'TCGA-E6-A1LX-01A-11D-A14G-09', 'Normal_SampleBarcode': 'TCGA-E6-A1LX-10A', 'Normal_AliquotBarcode': 'TCGA-E6-A1LX-10A-01D-A14G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R598Q', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1793G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Tumor_SampleBarcode': 'TCGA-EJ-7782-01A', 'Tumor_AliquotBarcode': 'TCGA-EJ-7782-01A-11D-2114-08', 'Normal_SampleBarcode': 'TCGA-EJ-7782-10A', 'Normal_AliquotBarcode': 'TCGA-EJ-7782-10A-01D-2114-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L249V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.745T>G', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Tumor_SampleBarcode': 'TCGA-FI-A2D5-01A', 'Tumor_AliquotBarcode': 'TCGA-FI-A2D5-01A-11D-A17D-09', 'Normal_SampleBarcode': 'TCGA-FI-A2D5-10A', 'Normal_AliquotBarcode': 'TCGA-FI-A2D5-10A-01D-A17D-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N785S', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.2354A>G', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Tumor_SampleBarcode': 'TCGA-G4-6628-01A', 'Tumor_AliquotBarcode': 'TCGA-G4-6628-01A-11D-1835-10', 'Normal_SampleBarcode': 'TCGA-G4-6628-10A', 'Normal_AliquotBarcode': 'TCGA-G4-6628-10A-01D-1835-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V425I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1273G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Tumor_SampleBarcode': 'TCGA-GI-A2C8-01A', 'Tumor_AliquotBarcode': 'TCGA-GI-A2C8-01A-11D-A16D-09', 'Normal_SampleBarcode': 'TCGA-GI-A2C8-11A', 'Normal_AliquotBarcode': 'TCGA-GI-A2C8-11A-22D-A16D-09', 'Normal_SampleTypeLetterCode': 'NT', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.W409L', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1226G>T', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Tumor_SampleBarcode': 'TCGA-VQ-A8PX-01A', 'Tumor_AliquotBarcode': 'TCGA-VQ-A8PX-01A-12D-A410-08', 'Normal_SampleBarcode': 'TCGA-VQ-A8PX-10A', 'Normal_AliquotBarcode': 'TCGA-VQ-A8PX-10A-01D-A413-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L776M', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.2326C>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
