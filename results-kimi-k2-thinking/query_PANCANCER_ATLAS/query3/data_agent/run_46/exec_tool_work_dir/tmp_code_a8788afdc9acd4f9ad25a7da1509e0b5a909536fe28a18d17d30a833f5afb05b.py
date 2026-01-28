code = """import json
import re
import pandas as pd
import numpy as np

# Load female BRCA patients data
clinical_path = globals()['var_functions.query_db:6']
with open(clinical_path, 'r') as f:
    clinical_records = json.load(f)

# Process clinical data to extract barcodes and histological types
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
mutation_path = globals()['var_functions.query_db:24']
with open(mutation_path, 'r') as f:
    mutation_records = json.load(f)

# Filter for reliable mutations (FILTER = PASS)
cdh1_pass_mutations = [r for r in mutation_records if r.get('FILTER') == 'PASS']

# Create mutation status mapping
mutation_status = {}
for record in cdh1_pass_mutations:
    barcode = record.get('ParticipantBarcode')
    if barcode:
        mutation_status[barcode] = True

# Add mutation status to patients
for patient in patients:
    patient['has_cdh1_mutation'] = patient['barcode'] in mutation_status

# Filter for patients with known histological types
patients_with_hist = [p for p in patients if p['histological_type'] and p['histological_type'] not in ['None', 'null', '']]

print('Patients with histological types: ' + str(len(patients_with_hist)))

# Create contingency table
contingency_data = []
for patient in patients_with_hist:
    contingency_data.append({
        'hist_type': patient['histological_type'],
        'cdh1_mut': 1 if patient['has_cdh1_mutation'] else 0
    })

df = pd.DataFrame(contingency_data)
contingency_table = pd.crosstab(df['hist_type'], df['cdh1_mut'])

print('Contingency table:')
print(contingency_table)

# Filter by row totals > 10
row_totals = contingency_table.sum(axis=1)
valid_types = row_totals[row_totals > 10].index.tolist()
filtered_table = contingency_table.loc[valid_types]

print('Filtered table:')
print(filtered_table)

# Calculate chi-square statistic manually
chi2 = None
df_val = None

if filtered_table.shape[0] >= 2 and filtered_table.shape[1] >= 2:
    observed = filtered_table.values
    row_sums = filtered_table.sum(axis=1).values
    col_sums = filtered_table.sum(axis=0).values
    grand_total = filtered_table.sum().sum()
    
    expected = np.outer(row_sums, col_sums) / grand_total
    chi2 = np.sum((observed - expected)  ** 2 / expected)
    df_val = (filtered_table.shape[0] - 1) * (filtered_table.shape[1] - 1)
    
    print('Chi-square: ' + str(round(chi2, 4)))
    print('DF: ' + str(df_val))

result = {
    'filtered_table': filtered_table.to_dict(),
    'chi2': float(chi2) if chi2 else None,
    'df': int(df_val) if df_val else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': 'Variable check complete', 'var_functions.execute_python:22': {'status': 'ready for mutation query'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
