code = """import json
import pandas as pd
import re
from scipy.stats import chi2_contingency

# Load female breast cancer clinical data
with open('var_functions.query_db:56', 'r') as f:
    clinical_data = json.load(f)

# Load CDH1 mutation data
with open('var_functions.query_db:44', 'r') as f:
    mutation_data = json.load(f)

print('Data loaded successfully')
print(f'Clinical records: {len(clinical_data)}')
print(f'Mutation records: {len(mutation_data)}')

# Create DataFrames
df_clinical = pd.DataFrame(clinical_data)
df_mutations = pd.DataFrame(mutation_data)

# Extract ParticipantBarcode from Patient_description in clinical data
def extract_barcode(desc):
    if pd.isna(desc):
        return None
    match = re.search(r'(TCGA-\w{2}-\w{4})', str(desc))
    if match:
        return match.group(1)
    return None

df_clinical['ParticipantBarcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter for valid histological types
df_clinical = df_clinical[df_clinical['histological_type'].notna() & (df_clinical['histological_type'] != '') & (df_clinical['histological_type'] != 'None')]
print(f'Clinical patients with known histological type: {len(df_clinical)}')

# Create mutation status indicator for CDH1
cdh1_mutants = set(df_mutations['ParticipantBarcode'].tolist())
df_clinical['CDH1_mutation'] = df_clinical['ParticipantBarcode'].apply(lambda x: 'Mutated' if x in cdh1_mutants else 'Wildtype')

# Count patients by histological type and mutation status
contingency_table = pd.crosstab(df_clinical['histological_type'], df_clinical['CDH1_mutation'])
print('\nInitial contingency table:')
print(contingency_table)

# Calculate marginal totals
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
grand_total = contingency_table.sum().sum()

print(f'\nGrand total: {grand_total}')
print(f'Row totals: {dict(row_totals)}')
print(f'Column totals: {dict(col_totals)}')

# Filter out histological types with row total <= 10
valid_histological_types = row_totals[row_totals > 10].index
filtered_table = contingency_table.loc[valid_histological_types]

print(f'\nAfter filtering histological types with >10 patients:')
print(filtered_table)

# Check if we have enough data for chi-square test
if filtered_table.shape[0] < 2 or filtered_table.shape[1] < 2:
    print('\nERROR: Not enough categories after filtering')
    result = {'error': 'Insufficient data after filtering categories with <=10 patients'}
else:
    # Calculate chi-square statistic
    chi2, p_value, dof, expected = chi2_contingency(filtered_table)
    
    print(f'\nChi-square results:')
    print(f'Chi-square statistic: {chi2:.4f}')
    print(f'p-value: {p_value:.4f}')
    print(f'Degrees of freedom: {dof}')
    print(f'Expected frequencies:')
    print(pd.DataFrame(expected, index=filtered_table.index, columns=filtered_table.columns))
    
    result = {
        'chi_square_statistic': float(chi2),
        'p_value': float(p_value),
        'degrees_of_freedom': int(dof),
        'contingency_table': filtered_table.to_dict(),
        'expected_frequencies': pd.DataFrame(expected, index=filtered_table.index, columns=filtered_table.columns).to_dict(),
        'total_patients_analyzed': int(filtered_table.sum().sum()),
        'histological_types_analyzed': int(filtered_table.shape[0])
    }

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:20': [], 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [], 'var_functions.query_db:38': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'count': '777'}, {'histological_type': 'Serous Cystadenocarcinoma', 'count': '584'}, {'histological_type': 'None', 'count': '563'}, {'histological_type': 'Untreated primary (de novo) GBM', 'count': '539'}, {'histological_type': 'Kidney Clear Cell Renal Carcinoma', 'count': '518'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma', 'count': '512'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type', 'count': '480'}, {'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'count': '470'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma', 'count': '401'}, {'histological_type': 'Colon Adenocarcinoma', 'count': '378'}, {'histological_type': 'Hepatocellular Carcinoma', 'count': '364'}, {'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual', 'count': '356'}, {'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)', 'count': '320'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma', 'count': '286'}, {'histological_type': 'Cervical Squamous Cell Carcinoma', 'count': '254'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'count': '201'}, {'histological_type': 'Astrocytoma', 'count': '194'}, {'histological_type': 'Oligodendroglioma', 'count': '189'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)', 'count': '162'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type', 'count': '153'}, {'histological_type': 'Pheochromocytoma', 'count': '147'}, {'histological_type': 'Rectal Adenocarcinoma', 'count': '140'}, {'histological_type': 'Oligoastrocytoma', 'count': '130'}, {'histological_type': 'Serous endometrial adenocarcinoma', 'count': '109'}, {'histological_type': 'Lung Adenocarcinoma Mixed Subtype', 'count': '107'}, {'histological_type': 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)', 'count': '102'}, {'histological_type': 'Leiomyosarcoma (LMS)', 'count': '101'}, {'histological_type': 'Esophagus Squamous Cell Carcinoma', 'count': '95'}, {'histological_type': 'Esophagus Adenocarcinoma  NOS', 'count': '88'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
