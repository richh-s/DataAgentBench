code = """import json
import re
import pandas as pd
import numpy as np

# Access stored data
vars_dict = globals()

# Load female BRCA patients data
clinical_key = 'var_functions.query_db:6'
clinical_path = vars_dict[clinical_key]
with open(clinical_path, 'r') as f:
    clinical_records = json.load(f)

print('Total clinical records:', len(clinical_records))

# Process clinical data
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

print('Total female BRCA patients:', len(patients))

# Load CDH1 mutation data
mutation_key = 'var_functions.query_db:24'
mutation_path = vars_dict[mutation_key]
with open(mutation_path, 'r') as f:
    mutation_records = json.load(f)

print('Total CDH1 mutations found:', len(mutation_records))

# Filter for reliable mutations (FILTER = PASS)
cdh1_pass_mutations = [record for record in mutation_records if record.get('FILTER') == 'PASS']
print('Reliable CDH1 mutations (FILTER=PASS):', len(cdh1_pass_mutations))

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
patients_with_hist = [p for p in patients if p['histological_type'] and p['histological_type'] not in ['None', 'null', '']]
print('Patients with known histological types:', len(patients_with_hist))

# Show histological type distribution
hist_counts = {}
for p in patients_with_hist:
    hist_type = p['histological_type']
    hist_counts[hist_type] = hist_counts.get(hist_type, 0) + 1

print('Histological type distribution:')
for hist_type, count in sorted(hist_counts.items(), key=lambda x: x[1], reverse=True):
    print(' ', hist_type, ':', count)

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

print('\nRow totals:')
for hist_type, total in row_totals.items():
    print(' ', hist_type, ':', total)

print('\nColumn totals:')
print(col_totals)
print('Grand total:', grand_total)

# Filter out categories with marginal totals <= 10
valid_hist_types = row_totals[row_totals > 10].index.tolist()
filtered_table = contingency_table.loc[valid_hist_types]

print('\nFiltered contingency table (row totals > 10):')
print(filtered_table)

# Calculate chi-square statistic manually
chi2_statistic = None
dof = None

if filtered_table.shape[0] >= 2 and filtered_table.shape[1] >= 2:
    observed = filtered_table.values
    row_totals_array = filtered_table.sum(axis=1).values
    col_totals_array = filtered_table.sum(axis=0).values
    
    # Calculate expected frequencies
    expected = np.outer(row_totals_array, col_totals_array) / grand_total
    
    # Calculate chi-square statistic
    chi2_statistic = np.sum((observed - expected) ** 2 / expected)
    
    # Calculate degrees of freedom
    dof = (filtered_table.shape[0] - 1) * (filtered_table.shape[1] - 1)
    
    print('\nExpected frequencies:')
    expected_df = pd.DataFrame(expected, index=filtered_table.index, columns=filtered_table.columns)
    print(expected_df)
    
    print('\nChi-square statistic:', round(chi2_statistic, 4))
    print('Degrees of freedom:', dof)
else:
    print('\nInsufficient data for chi-square test')

# Prepare results
result_table = {}
for idx, row in filtered_table.iterrows():
    result_table[str(idx)] = {'No': int(row.get('No', 0)), 'Yes': int(row.get('Yes', 0))}

result = {
    'contingency_table': result_table,
    'chi2_statistic': float(chi2_statistic) if chi2_statistic is not None else None,
    'degrees_of_freedom': int(dof) if dof is not None else None,
    'sample_size': int(grand_total)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': 'Variable check complete', 'var_functions.execute_python:22': {'status': 'ready for mutation query'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
