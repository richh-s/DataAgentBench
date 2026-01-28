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
    raise ValueError("Female BRCA clinical data not found")

clinical_path = vars_dict[clinical_key]
if isinstance(clinical_path, str) and clinical_path.endswith('.json'):
    with open(clinical_path, 'r') as f:
        clinical_records = json.load(f)
else:
    raise ValueError("Clinical data path not found or invalid")

# Process clinical data - extract patient barcodes and histological types
patients = []
for record in clinical_records:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    # Extract patient barcode
    match = re.search(r'(TCGA-\w+-\w+)', desc)
    if match:
        patients.append({
            'barcode': match.group(1),
            'histological_type': hist_type.strip()
        })

print(f"Total female BRCA patients: {len(patients)}")

# Load CDH1 mutation data
mutation_key = 'var_functions.query_db:24'
if mutation_key not in vars_dict:
    raise ValueError("CDH1 mutation data not found")

mutation_path = vars_dict[mutation_key]
if isinstance(mutation_path, str) and mutation_path.endswith('.json'):
    with open(mutation_path, 'r') as f:
        mutation_records = json.load(f)
else:
    raise ValueError("Mutation data path not found or invalid")

# Process mutations - keep only reliable calls (FILTER = 'PASS')
print(f"Total CDH1 mutations found: {len(mutation_records)}")

# Filter for reliable mutations
cdh1_pass_mutations = [
    record for record in mutation_records 
    if record.get('FILTER') == 'PASS'
]

print(f"Reliable CDH1 mutations (FILTER='PASS'): {len(cdh1_pass_mutations)}")

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

# Filter for patients with known histological types
valid_hist_types = ['Infiltrating Ductal Carcinoma', 'Infiltrating Lobular Carcinoma', 
                   'Mixed', 'Other', 'Mucinous Carcinoma', 'Medullary Carcinoma']

# Filter patients with non-empty histological types
patients_with_hist = [
    p for p in patients 
    if p['histological_type'] and p['histological_type'] not in ['None', 'null', '']
]

print(f"Patients with known histological types: {len(patients_with_hist)}")
print('Histological type distribution:')
hist_counts = {}
for p in patients_with_hist:
    hist_type = p['histological_type']
    hist_counts[hist_type] = hist_counts.get(hist_type, 0) + 1

for hist_type, count in sorted(hist_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {hist_type}: {count}")

# Create contingency table
contingency_data = []
for patient in patients_with_hist:
    contingency_data.append({
        'histological_type': patient['histological_type'],
        'cdh1_mutation': 'Yes' if patient['has_cdh1_mutation'] else 'No'
    })

df = pd.DataFrame(contingency_data)
contingency_table = pd.crosstab(df['histological_type'], df['cdh1_mutation'])

print('\nInitial contingency table:')
print(contingency_table)

# Calculate marginal totals
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
grand_total = contingency_table.sum().sum()

print(f'\nRow totals:')
for hist_type, total in row_totals.items():
    print(f"  {hist_type}: {total}")

print(f'\nColumn totals:')
print(col_totals)
print(f'Grand total: {grand_total}')

# Filter out categories with marginal totals <= 10
# Keep only histological types with row totals > 10
valid_hist_types = row_totals[row_totals > 10].index.tolist()
filtered_table = contingency_table.loc[valid_hist_types]

print('\nFiltered contingency table (excluded row totals <= 10):')
print(filtered_table)

# Check if we have enough data for chi-square test
if filtered_table.shape[0] < 2 or filtered_table.shape[1] < 2:
    print('\nInsufficient data for chi-square test after filtering')
    chi2 = None
    p_value = None
else:
    # Calculate chi-square statistic
    chi2, p_value, dof, expected = chi2_contingency(filtered_table)
    
    print(f"\nChi-square statistic: {chi2:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Degrees of freedom: {dof}")
    print('\nExpected frequencies:')
    print(pd.DataFrame(expected, index=filtered_table.index, columns=filtered_table.columns))

# Save results
result = {
    'contingency_table': filtered_table.to_dict(),
    'row_totals': row_totals[valid_hist_types].to_dict(),
    'col_totals': col_totals.to_dict(),
    'grand_total': int(grand_total),
    'chi2_statistic': float(chi2) if chi2 is not None else None,
    'p_value': float(p_value) if p_value is not None else None,
    'degrees_of_freedom': int(dof) if 'dof' in locals() else None
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': 'Variable check complete', 'var_functions.execute_python:22': {'status': 'ready for mutation query'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
