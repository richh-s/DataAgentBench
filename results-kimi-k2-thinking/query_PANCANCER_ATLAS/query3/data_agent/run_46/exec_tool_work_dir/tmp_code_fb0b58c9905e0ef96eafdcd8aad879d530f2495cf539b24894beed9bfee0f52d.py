code = """import json
import re
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

# Access stored data
vars_dict = globals()

# Load female BRCA patients data
clinical_key = 'var_functions.query_db:6'
if clinical_key not in vars_dict:
    print('ERROR: Female BRCA clinical data not found')
    result = {'error': 'Clinical data not found'}
else:
    clinical_path = vars_dict[clinical_key]
    if isinstance(clinical_path, str) and clinical_path.endswith('.json'):
        with open(clinical_path, 'r') as f:
            clinical_records = json.load(f)
    else:
        print('ERROR: Invalid clinical data path')
        result = {'error': 'Invalid clinical data path'}

# Process clinical data
patients = []
for record in clinical_records:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    match = re.search(r'(TCGA-\w+-\w+)', desc)
    if match:
        patients.append({
            'barcode': match.group(1),
            'histological_type': hist_type.strip()
        })

print('Total female BRCA patients: ' + str(len(patients)))

# Load CDH1 mutation data
mutation_key = 'var_functions.query_db:24'
if mutation_key not in vars_dict:
    print('ERROR: CDH1 mutation data not found')
    result = {'error': 'Mutation data not found'}
else:
    mutation_path = vars_dict[mutation_key]
    if isinstance(mutation_path, str) and mutation_path.endswith('.json'):
        with open(mutation_path, 'r') as f:
            mutation_records = json.load(f)
    else:
        print('ERROR: Invalid mutation data path')
        result = {'error': 'Invalid mutation data path'}

print('Total CDH1 mutations found: ' + str(len(mutation_records)))

# Filter for reliable mutations
cdh1_pass_mutations = [record for record in mutation_records if record.get('FILTER') == 'PASS']
print('Reliable CDH1 mutations (FILTER=PASS): ' + str(len(cdh1_pass_mutations)))

# Create mutation status mapping
mutation_status = {}
for record in cdh1_pass_mutations:
    barcode = record.get('ParticipantBarcode')
    if barcode:
        mutation_status[barcode] = True

# Add mutation status to patients
for patient in patients:
    barcode = patient['barcode']
    patient['has_cdh1_mutation'] = barcode in mutation_status

# Filter patients with non-empty histological types
patients_with_hist = [p for p in patients if p['histological_type'] and p['histological_type'] not in ['None', 'null', '']]
print('Patients with known histological types: ' + str(len(patients_with_hist)))

# Create contingency table
contingency_data = []
for patient in patients_with_hist:
    contingency_data.append({
        'histological_type': patient['histological_type'],
        'cdh1_mutation': 'Yes' if patient['has_cdh1_mutation'] else 'No'
    })

df = pd.DataFrame(contingency_data)
contingency_table = pd.crosstab(df['histological_type'], df['cdh1_mutation'])

print('Initial contingency table:')
print(contingency_table)

# Calculate marginal totals
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
grand_total = contingency_table.sum().sum()

print('Row totals:')
for hist_type, total in row_totals.items():
    print('  ' + str(hist_type) + ': ' + str(total))

print('Column totals:')
print(col_totals)
print('Grand total: ' + str(grand_total))

# Filter out categories with marginal totals <= 10
valid_hist_types = row_totals[row_totals > 10].index.tolist()
filtered_table = contingency_table.loc[valid_hist_types]

print('Filtered contingency table:')
print(filtered_table)

# Calculate chi-square statistic if we have enough data
chi2 = None
p_value = None
dof = None

if filtered_table.shape[0] >= 2 and filtered_table.shape[1] >= 2:
    chi2, p_value, dof, expected = chi2_contingency(filtered_table)
    print('Chi-square statistic: ' + str(chi2))
    print('p-value: ' + str(p_value))
    print('Degrees of freedom: ' + str(dof))
else:
    print('Insufficient data for chi-square test')

# Save results
result = {
    'contingency_table': filtered_table.to_dict(),
    'row_totals': {str(k): int(v) for k, v in row_totals[valid_hist_types].items()},
    'col_totals': {str(k): int(v) for k, v in col_totals.items()},
    'grand_total': int(grand_total),
    'chi2_statistic': float(chi2) if chi2 is not None else None,
    'p_value': float(p_value) if p_value is not None else None,
    'degrees_of_freedom': int(dof) if dof is not None else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': 'Variable check complete', 'var_functions.execute_python:22': {'status': 'ready for mutation query'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
