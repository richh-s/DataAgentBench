code = """import json
import pandas as pd
import numpy as np

# Load the data
with open('file_storage/functions.query_db:20.json', 'r') as f:
    clinical_data = json.load(f)

with open('file_storage/functions.query_db:25.json', 'r') as f:
    mutation_data = json.load(f)

# Create DataFrames
clinical_df = pd.DataFrame(clinical_data)
mutation_df = pd.DataFrame(mutation_data)

# Extract patient barcodes from clinical data
def extract_barcode(patient_desc):
    if 'TCGA-' in patient_desc:
        parts = patient_desc.split('TCGA-')
        for part in parts[1:]:
            barcode = 'TCGA-' + part.split()[0]
            return barcode
    return None

clinical_df['ParticipantBarcode'] = clinical_df['Patient_description'].apply(extract_barcode)
clinical_df = clinical_df[clinical_df['ParticipantBarcode'].notna()]

# Get CDH1 mutated participants
cdh1_mutated = set(mutation_df['ParticipantBarcode'].tolist())
clinical_df['CDH1_Mutated'] = clinical_df['ParticipantBarcode'].isin(cdh1_mutated)

# Create contingency table
contingency = pd.crosstab(clinical_df['histological_type'], clinical_df['CDH1_Mutated'])
contingency.columns = ['No_Mutation', 'Mutation']

# Calculate marginal totals
row_totals = contingency.sum(axis=1)
col_totals = contingency.sum(axis=0)
grand_total = contingency.values.sum()

# Filter histological types with > 10 patients
filtered_contingency = contingency[row_totals > 10]

# Manual chi-square calculation
def chi_square_test(contingency_table):
    row_sums = contingency_table.sum(axis=1).values
    col_sums = contingency_table.sum(axis=0).values
    grand_sum = contingency_table.values.sum()
    
    # Expected frequencies
    expected = np.outer(row_sums, col_sums) / grand_sum
    
    # Chi-square statistic
    chi2 = np.sum((contingency_table.values - expected) ** 2 / expected)
    
    # Degrees of freedom
    dof = (contingency_table.shape[0] - 1) * (contingency_table.shape[1] - 1)
    
    return chi2, dof, expected

chi2_statistic, dof, expected = chi_square_test(filtered_contingency)

result = {
    'chi2_statistic': float(chi2_statistic),
    'degrees_of_freedom': int(dof),
    'contingency_table': filtered_contingency.to_dict(),
    'expected_frequencies': expected.tolist(),
    'total_patients': int(grand_total),
    'cdh1_mutated_patients': int(col_totals['Mutation']),
    'cdh1_wildtype_patients': int(col_totals['No_Mutation'])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.query_db:6': [{'column_name': 'Patient_description'}, {'column_name': 'histological_type'}], 'var_functions.query_db:8': [{'patient_id': '1953', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31'}, {'patient_id': '1576', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '36'}, {'patient_id': '2408', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '25'}, {'patient_id': '2427', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '29'}, {'patient_id': '0933', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '10'}, {'patient_id': '1124', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '23'}, {'patient_id': '2641', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '23'}, {'patient_id': '1118', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '23'}, {'patient_id': '1120', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '23'}, {'patient_id': '2081', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '23'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A20V'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A9SX'}, {'Patient_description': 'Record 234086DD-5A74-4FF1-94AB-BAD43EE69D5C refers to patient TCGA-DK-A2I2, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A2I2'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A8HH (UUID 02964D82-CC94-4286-A66F-03567101950C) is recorded as a FEMALE with vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A8HH'}, {'Patient_description': 'The individual with barcode TCGA-ZF-A9R7 and UUID CE4E4549-BEFC-447F-9B79-ED46E302E6D7 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A9R7'}, {'Patient_description': "Patient TCGA-XF-AAME, registered under UUID C8388AC0-975D-4F1E-8324-8CABDC75738D, belongs to the Bladder urothelial carcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AAME'}, {'Patient_description': 'Clinical entry EDC290BF-9731-4F03-BC37-64542E78E8BB identifies patient TCGA-XF-AAMX, a FEMALE subject with Bladder urothelial carcinoma. Their current vital status is Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AAMX'}, {'Patient_description': 'Case 0DB0F02F-94F5-492F-8840-5254792F6879, linked to barcode TCGA-CF-A47T, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A47T'}, {'Patient_description': "Patient TCGA-FD-A5BU, registered under UUID 980C7214-F708-4499-818D-F3DE87DC6DE7, belongs to the Bladder urothelial carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A5BU'}, {'Patient_description': 'Case 32EFE5E2-E037-4547-8EAD-619F61647639, linked to barcode TCGA-K4-A5RI, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A5RI'}, {'Patient_description': 'The individual with barcode TCGA-KQ-A41R and UUID E492D5A9-7EC5-454B-AE89-077C90F67489 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A41R'}, {'Patient_description': 'Patient TCGA-XF-A9SI (UUID 6B0C8E8D-8ABA-413D-85ED-631653F00CA9) is a FEMALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A9SI'}, {'Patient_description': 'Patient TCGA-FD-A5BZ (UUID AC187CD1-A5EF-47DA-88B2-1D4DF27E0E76) is a FEMALE diagnosed with Bladder urothelial carcinoma. Current vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A5BZ'}, {'Patient_description': "Patient TCGA-5N-A9KM, registered under UUID 9743E684-25DD-4DD9-9B84-6AE9518D1818, belongs to the Bladder urothelial carcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A9KM'}, {'Patient_description': 'Patient TCGA-XF-AAMZ (UUID ED36D054-53C4-465C-BD84-6EC5227097BF) is a FEMALE diagnosed with Bladder urothelial carcinoma. Current vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AAMZ'}, {'Patient_description': 'Case 22424A05-0546-44C2-8AB7-ABB8E49C3363, linked to barcode TCGA-G2-AA3B, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AA3B'}, {'Patient_description': 'Clinical entry C1591625-E794-4155-8AE4-B74D6264659F identifies patient TCGA-XF-AAN5, a FEMALE subject with Bladder urothelial carcinoma. Their current vital status is Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AAN5'}, {'Patient_description': 'Case F78CB4FA-5548-40F8-B71B-663DDE47F539, linked to barcode TCGA-ZF-AA5N, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AA5N'}, {'Patient_description': 'Record 6BDDAFDE-7004-49B6-80CF-8081CD4B7D44 refers to patient TCGA-DK-A3X1, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'A3X1'}, {'Patient_description': 'Patient TCGA-YF-AA3L (UUID 661967E5-94B3-4F98-9402-6AB137893C16) is a FEMALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'patient_id': 'AA3L'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:19': ['clinical_info'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.execute_python:34': {'clinical_type': "<class 'str'>", 'mutation_type': "<class 'str'>", 'clinical_is_str': True, 'mutation_is_str': True}, 'var_functions.execute_python:38': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.list_db:19', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:25', 'var_functions.execute_python:34', '__builtins__', 'json'], 'globals': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.list_db:19', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:25', 'var_functions.execute_python:34', '__builtins__', 'json', 'available_vars']}, 'var_functions.execute_python:40': {'clinical_is_string': True, 'mutation_is_string': True, 'clinical_value': 'file_storage/functions.query_db:20.json', 'mutation_value_length': 'file_storage/functions.query_db:25.json'}, 'var_functions.execute_python:44': {'clinical_records': 108, 'mutation_records': 261, 'clinical_columns': ['Patient_description', 'histological_type', 'patient_id'], 'mutation_columns': ['ParticipantBarcode', 'Hugo_Symbol', 'FILTER']}}

exec(code, env_args)
