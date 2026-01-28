code = """import json
import math

# Load the analysis data from previous step
analysis_result = var_functions.execute_python:24
if isinstance(analysis_result, str):
    with open(analysis_result, 'r') as f:
        analysis_result = json.load(f)

contingency = analysis_result['contingency_table']

# Build 2xN contingency table matrix
# Rows: CDH1 mutation status (Yes/No)
# Columns: Histological types

histological_types = [row['histological_type'] for row in contingency]
observed_with_cdh1 = [row['with_cdh1'] for row in contingency]
observed_without_cdh1 = [row['without_cdh1'] for row in contingency]

total_with_cdh1 = sum(observed_with_cdh1)
total_without_cdh1 = sum(observed_without_cdh1)
total_patients = total_with_cdh1 + total_without_cdh1

# Calculate expected frequencies for each cell
# Eij = (row_total * col_total) / grand_total

col_totals = [row['total'] for row in contingency]

expected_with_cdh1 = []
expected_without_cdh1 = []

for i, col_total in enumerate(col_totals):
    # Expected for "with CDH1" row
    exp_with = (total_with_cdh1 * col_total) / total_patients
    expected_with_cdh1.append(exp_with)
    
    # Expected for "without CDH1" row
    exp_without = (total_without_cdh1 * col_total) / total_patients
    expected_without_cdh1.append(exp_without)

# Calculate chi-square statistic
chi_square = 0
chi_square_components = []

for i in range(len(histological_types)):
    # For "with CDH1" row
    obs = observed_with_cdh1[i]
    exp = expected_with_cdh1[i]
    if exp > 0:
        component = ((obs - exp) ** 2) / exp
        chi_square += component
        chi_square_components.append({
            'hist_type': histological_types[i],
            'mutation_status': 'with_cdh1',
            'observed': obs,
            'expected': round(exp, 2),
            'component': round(component, 4)
        })
    
    # For "without CDH1" row
    obs = observed_without_cdh1[i]
    exp = expected_without_cdh1[i]
    if exp > 0:
        component = ((obs - exp) ** 2) / exp
        chi_square += component
        chi_square_components.append({
            'hist_type': histological_types[i],
            'mutation_status': 'without_cdh1',
            'observed': obs,
            'expected': round(exp, 2),
            'component': round(component, 4)
        })

# Degrees of freedom = (rows - 1) * (columns - 1) = (2-1) * (N-1) = N-1
df = len(histological_types) - 1

result = {
    'chi_square_statistic': round(chi_square, 4),
    'degrees_of_freedom': df,
    'total_patients': total_patients,
    'total_with_cdh1': total_with_cdh1,
    'total_without_cdh1': total_without_cdh1,
    'contingency_table': contingency,
    'chi_square_components': chi_square_components,
    'expected_frequencies': {
        'with_cdh1': [round(x, 2) for x in expected_with_cdh1],
        'without_cdh1': [round(x, 2) for x in expected_without_cdh1]
    }
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-EW-A6SA and UUID ABA5F46A-E67A-4CD2-9C52-C0686968FF04 is a MALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A273 and UUID 5a5f0f48-2b13-4e78-b130-901b85d9a7f3 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record c2a742fe-3e8b-4210-85a6-7191a1123609 refers to patient TCGA-AN-A0FN, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FD, registered under UUID c6086936-7544-4da0-8c0c-114166848483, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 10c9be1e-2cc0-45e4-8d2c-c013ea63ef05 identifies patient TCGA-AN-A0FS, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'Record b5b99291-507e-4b68-a039-9a0f571f55df refers to patient TCGA-AO-A12H, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Other  specify'}, {'Patient_description': 'Record 3e9f93c0-aa79-4b4c-bd6c-b3325912362a refers to patient TCGA-AN-A0AL, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A3YI (UUID A45D296E-EFC0-479E-B2F6-BAD834668CDF) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-C8-A137, registered under UUID 03ab1e9f-4918-404d-b178-3a4fd929c5e8, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 0DD8DBC1-C48B-4E7C-B401-57101F724967 identifies patient TCGA-S3-AA11, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:24': {'total_patients': 1075, 'cdh1_mutations': 100, 'contingency_table': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'with_cdh1': 9, 'total': 766, 'without_cdh1': 757}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'with_cdh1': 83, 'total': 201, 'without_cdh1': 118}, {'histological_type': 'Mixed Histology (please specify)', 'with_cdh1': 4, 'total': 30, 'without_cdh1': 26}, {'histological_type': 'Mucinous Carcinoma', 'with_cdh1': 0, 'total': 17, 'without_cdh1': 17}, {'histological_type': 'Other  specify', 'with_cdh1': 3, 'total': 45, 'without_cdh1': 42}], 'hist_types_examined': 5}}

exec(code, env_args)
